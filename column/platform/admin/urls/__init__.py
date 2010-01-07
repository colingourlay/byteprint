from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout_then_login

urlpatterns = patterns('platform.admin.views',
    url(r'^$', 'portal', name='admin'),
    url(r'^login/$', login, {'template_name': 'admin/login.html',}, name='login'),
    url(r'^logout/$', logout_then_login, {'login_url': '/admin/login/'}, name='logout'),
    url(r'^settings/general/$', 'settings.general', name='admin_settings_general'),
    url(r'^blueprints/$', 'blueprints.list', name='admin_blueprints_list'),
    url(r'^widgets/build/(?P<blueprint_name>[\w-]+)/$', 'widgets.build', name='admin_widgets_build'),
    url(r'^widgets/(?P<widget_id>\d+)/$', 'widgets.edit', name='admin_widgets_edit'),
    url(r'^widgets/$', 'widgets.list', name='admin_widgets_list'),
)
