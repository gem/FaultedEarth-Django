from django.conf.urls.defaults import *
from geonode.observations.views import obsform

urlpatterns = patterns('geonode.observations.views',
    url(r'^obsform/new$', obsform),
    url(r'^obsform/$', obsform),
    (r'^(?P<mapid>\d+)/view$', 'view'),
    #(r'^admin/', include(admin.site.urls)),
)

