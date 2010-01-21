from django.conf.urls.defaults import *

urlpatterns = patterns('platform.core.site.views',
    url(r'^$', 'homepage', name='site_homepage'),
)