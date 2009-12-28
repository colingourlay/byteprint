from django.conf.urls.defaults import *

urlpatterns = patterns('platform.core.views',
    url(r'^$', 'homepage', name='core_homepage'),
)