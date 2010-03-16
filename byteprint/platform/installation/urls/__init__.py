from django.conf.urls.defaults import *

urlpatterns = patterns('platform.installation.views',
    url(r'^$',
        'init_platform',
        name='installation_init_platform'
    ),
)