from django import forms
from django.forms import ModelForm
from geonode.observations.models import Observations
#from geonode.observations.models import FaultSummary, ObservationType, Slip, Site, SlipType
"""
# a class for the original faulted_earth db
class ObsFormSlip (forms.Form):
    slip_type = forms.IntegerField()
    hv_ratio = forms.DecimalField(max_digits=3, decimal_places=2)
    rake = forms.IntegerField()
    dip_slip_rate = forms.DecimalField(max_digits=3, decimal_places=2)
    strike_slip_rate = forms.DecimalField(max_digits=3, decimal_places=2)
    vertical_slip_rate = forms.DecimalField(max_digits=3, decimal_places=2)
    marker_age = forms.IntegerField()
    
"""

class Observation(forms.ModelForm):
    class Meta:
        model = Observations
    