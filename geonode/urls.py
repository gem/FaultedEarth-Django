from django.conf.urls.defaults import *

urlpatterns = patterns('geonode.observations.views',
    (r'edit/(?P<observation_id>\d+)/summary_id/(?P<summary_id>\d+)$', 'edit'),
    (r'new/summary_id/(?P<summary_id>\d+)$', 'new'),
    (r'^$', 'obsform'),
)
