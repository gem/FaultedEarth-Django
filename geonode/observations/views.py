from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from geonode.observations.forms import Observation
from django.template import RequestContext
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

def new(request, summary_id):
    o = models.Observations(summary_id=summary_id)
    o.save()
    return render_to_response('new.html', {'observation' : o})


def edit(request, observation_id, summary_id):
    """  
    The view that returns the Id filed from the fault summary table.
    """
    o = get_object_or_404(models.Observations, pk=observation_id)
    o.summary_id = summary_id
    o.save()
    
    return render_to_response('edit.html', {'observation' : o})
