from django import forms
from django.forms import ModelForm
from geonode.observations.models import Observations, FaultSummary

class Observation(forms.ModelForm):
    class Meta:
        model = Observations
    
class Summary(forms.ModelForm):
    class Meta:
        model = FaultSummary