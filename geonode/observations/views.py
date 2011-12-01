# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2010-2011, GEM Foundation.
#
# OpenQuake is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# only, as published by the Free Software Foundation.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License version 3 for more details
# (a copy is included in the LICENSE file that accompanied this code).
#
# You should have received a copy of the GNU Lesser General Public License
# version 3 along with OpenQuake.  If not, see
# <http://www.gnu.org/licenses/lgpl-3.0.txt> for a copy of the LGPLv3 License

from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_response_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson

from geonode.observations import models
from geonode.observations.forms import Observation
from geonode.observations.utils import create_faultsource


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

def traces(request):

    response = HttpResponse()
    if request.is_ajax():
        if request.method == 'PUT':

            json_data = request.raw_post_data

            fault_section = models.FaultSection.objects.create()

            for trace in simplejson.loads(json_data):
                if isinstance(trace, dict):
                    fault_section.sec_name = trace['name']
                else:
                    trace = models.Trace.objects.get(pk=trace.split('.')[1])
                    trace.fault_section.add(fault_section)

            fault_section.save()


    return response

def faultsection(request):
    response = HttpResponse()
    if request.is_ajax():
        if request.method == 'PUT':

            json_data = request.raw_post_data

            fault = models.Fault.objects.create()

            for fault_section_id in simplejson.loads(json_data):
                if isinstance(fault_section_id, dict):
                    fault.fault_name = fault_section_id['name']
                else:
                    fault_section = models.FaultSection.objects.get(
                            pk=fault_section_id)
                    fault_section.fault.add(fault)

            fault.save()

    return response


def faultsource(request):
    response = HttpResponse()
    if request.is_ajax():
        if request.method == 'PUT':

            json_data = simplejson.loads(request.raw_post_data)
            name = json_data['name']
            fault_id = json_data['fault_id']
            fault = models.Fault.objects.get(pk=fault_id)
            create_faultsource(fault, name)

    return response


def new(request, summary_id):
    o = models.Observations(summary_id=summary_id)
    o.save()

    return HttpResponseRedirect(
            '/observations/obsform/edit/%s/summary_id/%s' %
            (o.id, o.summary_id))


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
