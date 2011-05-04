from django import forms
from django.forms import ModelForm
from source.observations.models import ObservationModel
                
class Observation(forms.ModelForm):
    class Meta:
        model = ObservationModel