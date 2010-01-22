from django.conf.urls.defaults import *

urlpatterns = patterns('platform.admin.settings.views',
    url(r'^general/$',
        'general',
        name='admin_settings_general'
    ),
    url(r'^widgets/$',
        'widgets',
        name='admin_settings_widgets'
    ),
)