from django.conf.urls.defaults import *
from faultedearth.observations.views import obs_form_slip, obs_form_displacement, obsform

urlpatterns = patterns('',
    ('^obs_form_slip/$', obs_form_slip),
    ('^obs_form_displacement/$', obs_form_displacement),
    ('^obsform/$', obsform),
    #(r'^admin/', include(admin.site.urls)),
)