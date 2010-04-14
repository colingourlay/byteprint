from django.conf.urls.defaults import *

urlpatterns = patterns('bp.core.config.views.admin',
    url(r'^general/$',
        'general',
        name='config_admin_general'
    ),
    url(r'^scraps/$',
        'scraps',
        name='config_admin_scraps'
    ),
)