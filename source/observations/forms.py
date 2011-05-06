from django import forms
from django.forms import ModelForm
from source.observations.models import TempFormSlip
from source.observations.models import FaultSummary, ObservationType, Slip, Site, SlipType

class ObsFormSlip (forms.Form):
    slip_type = forms.IntegerField()
    hv_ratio = forms.DecimalField(max_digits=3, decimal_places=2)
    rake = forms.IntegerField()
    dip_slip_rate = forms.DecimalField(max_digits=3, decimal_places=2)
    strike_slip_rate = forms.DecimalField(max_digits=3, decimal_places=2)
    vertical_slip_rate = forms.DecimalField(max_digits=3, decimal_places=2)
    marker_age = forms.IntegerField()
    
      
class ObsFormDisplacement (forms.Form):
    aseismic_slip_factor = forms.IntegerField()
    dip_slip_rate = forms.DecimalField(max_digits=3, decimal_places=2)
    hv_ratio = forms.DecimalField(max_digits=3, decimal_places=2)
    marker_age = forms.IntegerField()
    rake = forms.IntegerField()
    
class Observation(forms.ModelForm):
    class Meta:
        model = TempFormSlip
    