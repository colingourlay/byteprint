from django.conf.urls.defaults import *

urlpatterns = patterns('bp.core.installation.views',
    url(r'^$',
        'install',
        name='installation_install'
    ),
)