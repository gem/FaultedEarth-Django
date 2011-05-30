from django.conf.urls.defaults import *

urlpatterns = patterns('geonode.observations.views',
   (r'^obsform/edit/(?P<observation_id>\d+)/summary_id/(?P<summary_id>\d+)$',
        'edit'),
   (r'^obsform/new/summary_id/(?P<summary_id>\d+)$',
        'new'),
)
