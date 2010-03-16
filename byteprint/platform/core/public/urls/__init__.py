from django.conf.urls.defaults import *

urlpatterns = patterns('platform.core.public.views',
    url(r'^$', 'homepage', name='public_homepage'),
)