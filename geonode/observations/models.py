from django.db import models

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
    observationType = models.CharField(max_length=1, choices=OBS_TYPE, 
    default='4')
    SLIP_TYPE = (
        ('0','Normal'),
    )
    slipType = models.CharField(max_length=1, choices=SLIP_TYPE, default='0')
    hv_ratio = models.CharField(max_length=100, default='1:3.75', blank=True)
    rake = models.CharField(max_length=100, blank=True)
    net_slip_rate_min = models.CharField(max_length=100, default='min', 
    blank=True)
    net_slip_rate_max = models.CharField(max_length=100, default='max', 
    blank=True)
    net_slip_rate_pref = models.CharField(max_length=100, default='pref', 
    blank=True)
    dip_slip_rate_min = models.CharField(max_length=100, default='min', 
    blank=True)
    dip_slip_rate_max = models.CharField(max_length=100, default='max', 
    blank=True)
    dip_slip_rate_pref = models.CharField(max_length=100, default='pref', 
    blank=True)
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
    default='0', blank=True)
    strike_slip_rate_min = models.CharField(max_length=100, default='min', 
    blank=True)
    strike_slip_rate_max = models.CharField(max_length=100, default='max', 
    blank=True)
    strike_slip_rate_pref = models.CharField(max_length=100, default='pref', 
    blank=True)
    vertical_slip_rate_min = models.CharField(max_length=100, default='min', 
    blank=True)
    vertical_slip_rate_max = models.CharField(max_length=100, default='max', 
    blank=True)
    vertical_slip_rate_pref = models.CharField(max_length=100, default='pref', 
    blank=True)
    site = models.CharField(max_length=100, default='-42.375, 176.543', 
    blank=True)
    notes = models.TextField(blank=True)
    summary_id = models.CharField(max_length=100, default='-1', blank=True)
    class Meta:
        db_table = 'gem\".\"observations_observations'
  
class FaultSummary(models.Model):
    name = models.IntegerField(max_length=100, default='-1', blank=True)
    class Meta:
        db_table = 'gem\".\"fault_summary'
