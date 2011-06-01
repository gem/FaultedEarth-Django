# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

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

from django.db import models

#observation db

class Observations(models.Model):
    OBS_TYPE = (
        ('0','Displacement'),
        ('1','Event'),
        ('2','Recurrence Interval'),
        ('3','Seismogenic Geometry'),
        ('4','SlipRate'),
    )
    observationType = models.CharField(max_length=1, choices=OBS_TYPE, 
    blank=True)
    SLIP_TYPE = (
        ('0','Reverse'),
        ('1','Thrust (dip <45)'),
        ('2','Normal'),
        ('3','Dextral'),
        ('4','Sinistral'),
        ('5','Normal dextral'),
        ('6','Normal sinistral'),
        ('7','Reverse dextral'),
        ('8','Reverse sinistral'),
        ('9','Dextral normal'),
        ('10','Dextral reverse'),
        ('11','Sinistral reverse'),
        ('12','Sinistral normal'),
    )
    slipType = models.CharField(max_length=1, choices=SLIP_TYPE,
                               blank=True)
    hv_ratio = models.CharField(max_length=100, blank=True)
    rake = models.CharField(max_length=100, blank=True)
    net_slip_rate_min = models.CharField(max_length=100, blank=True)
    net_slip_rate_max = models.CharField(max_length=100, blank=True)
    net_slip_rate_pref = models.CharField(max_length=100, blank=True)
    dip_slip_rate_min = models.CharField(max_length=100, blank=True)
    dip_slip_rate_max = models.CharField(max_length=100, blank=True)
    dip_slip_rate_pref = models.CharField(max_length=100, blank=True)
    marker_age = models.CharField(max_length=100, blank=True)
    SLIP_RATE_CAT = (
        ('0','0.001 <0.01'),
        ('1','0.01 <0.1'),
        ('2','0.1 <1'),
        ('3','1 <5'),
        ('4','5 <10'),
        ('5','10 <50'),
        ('6','50 <100'),
        ('7','100 <200'),
    )
    slip_rate_category = models.CharField(max_length=10, choices=SLIP_RATE_CAT, 
    blank=True)
    strike_slip_rate_min = models.CharField(max_length=100, blank=True)
    strike_slip_rate_max = models.CharField(max_length=100, blank=True)
    strike_slip_rate_pref = models.CharField(max_length=100, blank=True)
    vertical_slip_rate_min = models.CharField(max_length=100, blank=True)
    vertical_slip_rate_max = models.CharField(max_length=100, blank=True)
    vertical_slip_rate_pref = models.CharField(max_length=100, blank=True)
    site = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    summary_id = models.CharField(max_length=100,  blank=True)
    class Meta:
        db_table = 'gem\".\"observations_observations'
  
class FaultSummary(models.Model):
    fid = models.IntegerField()
    name = models.IntegerField(max_length=100, default='-1', blank=True)
    class Meta:
        db_table = 'gem\".\"fault_summary'
