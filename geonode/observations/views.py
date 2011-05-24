from django.shortcuts import render_to_response
from geonode.observations.forms import Observation
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from geonode.observations import models
   
#views for the observation form
def obsform(request):
    if request.method == 'POST':
        form = Observation(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("obsform_form.html",
                      {'form': form,
                       'success' : 'Your observation was saved'},
                context_instance=RequestContext(request))
    else:
        form = Observation()
    return render_to_response('obsform_form.html', {'form': form})


def view(request, name):
    """  
    The view that returns the Id filed from the fault summary table.
    """
    id = models.FaultSummary.objects.get(name) 
