from django.conf.urls.defaults import *
from geonode.observations.views import obsform, view

urlpatterns = patterns('geonode.observations.views',
    url(r'^obsform/new$', obsform),
    url(r'^obsform/$', obsform),
    url(r'^view/$', view),
    (r'^(?P<mapid>\d+)/view$', 'view'),
    url(r'^obsform/view/\d+$', view),
    #(r'^admin/', include(admin.site.urls)),
)

