from django.db import models
from django.forms import ModelForm

#temp observation db
#_______________________________________

class Observations(models.Model):
    OBS_TYPE = (
        ('0','Displacement'),
        ('1','Event'),
        ('2','Recurrence Interval'),
        ('3','Seismogenic Geometry'),
        ('4','SlipRate'),
    )
    observationType = models.CharField(max_length=1, choices=OBS_TYPE, default='4')
    SLIP_TYPE = (
        ('0','Normal'),
    )
    slipType = models.CharField(max_length=1, choices=SLIP_TYPE, default='0')
    hv_ratio = models.CharField(max_length=100, default='1:3.75')
    rake = models.CharField(max_length=100)
    net_slip_rate_min = models.CharField(max_length=100, default='min')
    net_slip_rate_max = models.CharField(max_length=100, default='max')
    net_slip_rate_pref = models.CharField(max_length=100, default='pref')
    dip_slip_rate_min = models.CharField(max_length=100, default='min')
    dip_slip_rate_max = models.CharField(max_length=100, default='max')
    dip_slip_rate_pref = models.CharField(max_length=100, default='pref')
    marker_age = models.CharField(max_length=100)
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
    slip_rate_category = models.CharField(max_length=10, choices=SLIP_RATE_CAT, default='0')
    strike_slip_rate_min = models.CharField(max_length=100, default='min')
    strike_slip_rate_max = models.CharField(max_length=100, default='max')
    strike_slip_rate_pref = models.CharField(max_length=100, default='pref')
    vertical_slip_rate_min = models.CharField(max_length=100, default='min')
    vertical_slip_rate_max = models.CharField(max_length=100, default='max')
    vertical_slip_rate_pref = models.CharField(max_length=100, default='pref')
    site = models.CharField(max_length=100, default='-42.375, 176.543')
    notes = models.TextField()
    class Meta:
        db_table = 'gem\".\"observations_observations'
