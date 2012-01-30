# coding: utf-8
#
#Copyright (C) 2012  FaultedEarth
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/agpl.html>.


import math

import jpype
import shapely
from django.contrib.gis.geos.collections import Polygon
from django.conf import settings

from geonode.observations import models


def fault_poly_from_mls(fault_source_geom, dip,
                        upp_seis_depth, low_seis_depth):
    """Given a fault source geometry (as a MultiLineString), dip, upper
    seismogenic depth, lower seismogenic depth, and grid spacing (in km),
    create a 3D polygon to represent the fault.

    :param fault_source_geom:
        :class:`django.contrib.gis.geos.collections.MultiLineString`
    :param float dip:
        Angle of dip, from 0.0 to 90.0 degrees (inclusive)
    :param float upp_seis_depth:
        Upper seismogenic depth
    :param float low_seis_depth:
        Lower seismogenic depth

    :returns:
        3D polygon representing the complete fault geometry
    :rtype:
        :class:`django.contrib.gis.geos.collections.Polygon`
    """
    # I take no responsibility for writing this

    #: Value is in kilometers
    GRID_SPACING = 1.0

    if not jpype.isJVMStarted():
        # start jvm once
        jpype.startJVM(jpype.getDefaultJVMPath(),
                       "-Djava.ext.dirs=%s" % settings.GEOCLUDGE_JAR_PATH)

    FT = jpype.JClass('org.opensha.sha.faultSurface.FaultTrace')
    LOC = jpype.JClass('org.opensha.commons.geo.Location')
    LOC_LIST = jpype.JClass('org.opensha.commons.geo.LocationList')
    SGS = jpype.JClass('org.opensha.sha.faultSurface.StirlingGriddedSurface')

    coords = fault_source_geom.coords

    fault_trace = FT('')
    for line_str in coords:
        for lon, lat in line_str:
            # warning: the ordering of lat/lon is switched here
            # be careful
            loc = LOC(lat, lon)
            fault_trace.add(loc)

    surface = SGS(fault_trace, float(dip),
                  float(upp_seis_depth), float(low_seis_depth),
                  GRID_SPACING)

    # now we make a polygon with the perimeter coords:
    poly_coords = []
    for per_loc in surface.getSurfacePerimeterLocsList():
        lon = per_loc.getLongitude()
        lat = per_loc.getLatitude()
        depth = per_loc.getDepth()

        poly_coords.append((lon, lat, depth))

    return Polygon(poly_coords)


def create_faultsource(fault, name):
    polygon = fault_poly_from_mls(
        fault.simple_geom, fault.dip_pref,
        fault.u_sm_d_pre, fault.low_d_pref
    )

    sin = lambda degrees: math.sin(math.radians(degrees))

    # these attributes are copied from the corresponding fault
    verbatim_attributes = """
    length_min length_max length_pre
    u_sm_d_min u_sm_d_max u_sm_d_pre u_sm_d_com
    low_d_min low_d_max low_d_pref low_d_com
    dip_min dip_max dip_pref dip_com dip_dir
    slip_typ slip_com slip_r_min slip_r_max slip_r_pre slip_r_com
    aseis_slip aseis_com
    mov_min mov_max mov_pref
    """.strip().split()

    a = dict((attrib_name, getattr(fault, attrib_name))
             for attrib_name in verbatim_attributes)
    a.update(dict(
        width_min=(a['low_d_min'] - a['u_sm_d_max']) / sin(a['dip_max']),
        width_max=(a['low_d_max'] - a['u_sm_d_min']) / sin(a['dip_min']),
        width_pref=(a['low_d_pref'] - a['u_sm_d_pre']) / sin(a['dip_pref']),
    ))
    a.update(dict(
        area_pref=a['length_pre'] * a['width_pref'],
        area_min=a['length_min'] * a['width_min'],
        area_max=a['length_max'] * a['width_max'],
    ))
    a.update(dict(
        # Magnitude scaling law is "New Zealand -- oblique slip"
        mag_min=(4.18
                 + 4.0 / 3.0 * math.log10(a['length_min'])
                 + 2.0 / 3.0 * math.log10(a['width_min'])),
        mag_max=(4.18
                 + 4.0 / 3.0 * math.log10(a['length_max'])
                 + 2.0 / 3.0 * math.log10(a['width_max'])),
        mag_pref=(4.18
                  + 4.0 / 3.0 * math.log10(a['length_pre'])
                  + 2.0 / 3.0 * math.log10(a['width_pref'])),
    ))
    a.update(dict(
        mom_min=10 ** (16.05 + (1.5 * a['mag_min'])),
        mom_max=10 ** (16.05 + (1.5 * a['mag_max'])),
        mom_pref=10 ** (16.05 + (1.5 * a['mag_pref'])),
    ))
    a.update(dict(
        dis_min=a['mom_min'] / (3.0e11 * a['area_min'] * 1.0e10) * 0.01,
        dis_max=a['mom_max'] / (3.0e11 * a['area_max'] * 1.0e10) * 0.01,
        dis_pref=a['mom_pref'] / (3.0e11 * a['area_pref'] * 1.0e10) * 0.01,
    ))
    a.update(dict(
        re_int_min=a['dis_min'] * 1e3 / a['slip_r_max'],
        re_int_max=a['dis_max'] * 1e3 / a['slip_r_min'],
        re_int_pre=a['dis_pref'] * 1e3 / a['slip_r_pre'],
    ))
    a.update(dict(
        all_com=(a['u_sm_d_com'] + a['low_d_com'] + a['dip_com'] + a['dip_dir']
                 + a['slip_com'] + 5 * a['slip_r_com'] + a['aseis_slip']) / 11
    ))

    faultsource = models.FaultSource.objects.create(
        fault=fault, source_nm=name, geom=polygon, **a
    )

    return faultsource
