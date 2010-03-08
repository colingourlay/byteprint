from django.conf.urls.defaults import *

urlpatterns = patterns('platform.public.views',
    url(r'^$', 'homepage', name='public_homepage'),
)