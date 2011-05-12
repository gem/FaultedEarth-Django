from django.conf.urls.defaults import *
from geonode.observations.views import obsform

urlpatterns = patterns('',
    #('^obs_form_slip/$', obs_form_slip),
    #('^obs_form_displacement/$', obs_form_displacement),
    ('^obsform/$', obsform),
    #(r'^admin/', include(admin.site.urls)),
)