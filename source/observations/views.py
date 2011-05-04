from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from source.observations.forms import Observation
from django.template import RequestContext
 
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
             