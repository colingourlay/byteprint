from django.conf.urls.defaults import *

urlpatterns = patterns('platform.admin.settings.views',
    url(r'^general/$',
        'general',
        name='admin_settings_general'
    ),
    url(r'^scraps/$',
        'scraps',
        name='admin_settings_scraps'
    ),
)