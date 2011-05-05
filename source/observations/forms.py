from django import forms
from django.forms import ModelForm
#from source.observations.models import ObservationModel
from source.observations.models import FaultSummary
           
class Observation(ModelForm):
    dip = forms.IntegerField() # This field type is a guess.
    class Meta:
        model = FaultSummary

        