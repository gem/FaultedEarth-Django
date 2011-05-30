from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from geonode.observations.forms import Observation
from django.template import RequestContext
from geonode.observations import models
from django.views.decorators.csrf import csrf_exempt, csrf_response_exempt
from django.http import HttpResponseRedirect

   
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
    return render_to_response('obsform_form.html', {'form': form},
                              context_instance=RequestContext(request))

def new(request, summary_id):
    o = models.Observations(summary_id=summary_id)
    o.save()

    return HttpResponseRedirect('/observations/obsform/edit/%s/summary_id/%s' % (o.id, o.summary_id))


def edit(request, observation_id, summary_id):
    """  
    The view that returns the Id filed from the fault summary table.
    """

    if request.method == 'POST':
        if observation_id and summary_id:
            o = get_object_or_404(models.Observations, pk=observation_id)
            o.summary_id = summary_id
            form = Observation(request.POST,instance=o)
        else:
            form = Observation(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("obsform_form.html",
                      {'form': form,
                       'success' : 'Your observation was saved'},
                context_instance=RequestContext(request))
    else:
        o = get_object_or_404(models.Observations, pk=observation_id)
        o.summary_id = summary_id

        form = Observation(instance=o)
    
    return render_to_response('obsform_form.html', {'form' : form},
                              context_instance=RequestContext(request))
