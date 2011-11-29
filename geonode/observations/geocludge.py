# coding: utf-8
#
# Copyright (c) 2010-2011, GEM Foundation.
#
# OpenQuake is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# only, as published by the Free Software Foundation.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License version 3 for more details
# (a copy is included in the LICENSE file that accompanied this code).
#
# You should have received a copy of the GNU Lesser General Public License
# version 3 along with OpenQuake.  If not, see
# <http://www.gnu.org/licenses/lgpl-3.0.txt> for a copy of the LGPLv3 License
#

# I take no responsibility for writing this

import jpype
import shapely
from django.contrib.gis.geos.collections import Polygon
from django.conf import settings


#: Value is in kilometers
GRID_SPACING = 1.0


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
    if not jpype.isJVMStarted():
        # start jvm once
        jpype.startJVM(jpype.getDefaultJVMPath(),
                       "-Djava.ext.dirs=%s" % settings.GEOCLUDGE_JAR_PATH)

    FT = jp.JClass('org.opensha.sha.faultSurface.FaultTrace')
    LOC = jp.JClass('org.opensha.commons.geo.Location')
    LOC_LIST = jp.JClass('org.opensha.commons.geo.LocationList')
    SGS = jp.JClass('org.opensha.sha.faultSurface.StirlingGriddedSurface')

    coords = fault_source_geom.coords

    fault_trace = FT('')
    for line_str in coords:
        for lon, lat in line_str:
            # warning: the ordering of lat/lon is switched here
            # be careful
            loc = LOC(lat, lon)
            fault_trace.add(loc)

    surface = SGS(fault_trace, dip, upp_seis_depth, low_seis_depth,
                  GRID_SPACING)

    # now we make a polygon with the perimeter coords:
    poly_coords = []
    for per_loc in surface.getSurfacePerimeterLocsList():
        lon = per_loc.getLongitude()
        lat = per_loc.getLatitude()
        depth = per_loc.getDepth()

        poly_coords.append((lon, lat, depth))

    return Polygon(poly_coords)
