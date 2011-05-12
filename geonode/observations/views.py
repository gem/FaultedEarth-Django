from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from geonode.observations.forms import Observation
from django.template import RequestContext

# Views for the original faulted_earth db  
"""           
def obs_form_slip (request):
    if request.method == 'GET':
        form = ObsFormSlip()
        if form.is_valid():
            form.save()
            return render_to_response("obsform_slip.html",
                {'form': form},
                context_instance=RequestContext(request))
    else:
        form = ObsFormSlip(
            initial={'subject': 'I love your site!'}
        )
    return render_to_response('obsform_slip.html', {'form': form})
    
def obs_form_displacement (request):
    if request.method == 'GET':
        form = ObsFormDisplacement()
        if form.is_valid():
            form.save()
            return render_to_response("obsform_displacement.html",
                {'form': form},
                context_instance=RequestContext(request))
    else:
        form = ObsFormDisplacement(
            initial={'subject': 'I love your site!'}
        )
    return render_to_response('obsform_displacement.html', {'form': form})
"""
   
#views for the observation db
def obsform(request):
    if request.method == 'POST':
        form = Observation(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("obsform_form.html",
                {'form': form},
                context_instance=RequestContext(request))
    else:
        form = Observation(
            initial={'subject': 'I love your site!'}
        )
    return render_to_response('obsform_form.html', {'form': form})