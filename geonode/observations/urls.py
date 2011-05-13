from django.conf.urls.defaults import *
from geonode.observations.views import obsform

urlpatterns = patterns('geonode.observations.views',
    #('^obs_form_slip/$', obs_form_slip),
    #('^obs_form_displacement/$', obs_form_displacement),
    url(r'^obsform/$', obsform),
    #(r'^admin/', include(admin.site.urls)),
)
