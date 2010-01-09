from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout_then_login

urlpatterns = patterns('platform.admin.views',
    url(r'^$', 'dashboard', name='admin'),
    url(r'^login/$', login, {'template_name': 'admin/login.html',}, name='login'),
    url(r'^logout/$', logout_then_login, {'login_url': '/admin/login/'}, name='logout'),
    url(r'^settings/general/$', 'settings.general', name='admin_settings_general'),
    url(r'^widgets/build/$', 'widgets.build', name='admin_widgets_build'),
    url(r'^widgets/(?P<widget_id>\d+)/delete/$', 'widgets.delete', name='admin_widgets_delete'),
    url(r'^widgets/(?P<widget_id>\d+)/$', 'widgets.edit', name='admin_widgets_edit'),
    url(r'^widgets/$', 'widgets.manage', name='admin_widgets_manage'),
)
