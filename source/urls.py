from django.conf.urls.defaults import *
from source.observations.views import obsform

urlpatterns = patterns('',
    ('^obsform/$', obsform),
    #(r'^admin/', include(admin.site.urls)),
)