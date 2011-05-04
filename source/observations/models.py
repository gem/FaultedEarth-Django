from django.db import models
       
class ObservationModel(models.Model):
    OBS_TYPE = (
        ('0','Displacement'),
        ('1','Event'),
        ('2','Recurrence Interval'),
        ('3','Seismogenic Geometry'),
        ('4','SlipRate'),
    )
    observationType = models.CharField(max_length=1, choices=OBS_TYPE, default='0')
    aseismicSlipFactor = models.CharField(max_length=100, default='pref, min, max')
    dip_slip_rate = models.CharField(max_length=100, default='pref, min, max')
    hv_ratio = models.CharField(max_length=100, default='1:3.75')
    marker_age = models.CharField(max_length=100)
    rake = models.CharField(max_length=100)
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
    strike_slip_rate = models.CharField(max_length=100, default='pref, min, max')
    vertical_slip_rate = models.CharField(max_length=100, default='pref, min, max')
    site = models.CharField(max_length=100, default='-42.375, 176.543')
    notes = models.TextField()
