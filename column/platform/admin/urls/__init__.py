from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout_then_login

urlpatterns = patterns('platform.admin.views',
    url(r'^$', 'portal', name='admin'),
    url(r'^login/$', login, {'template_name': 'admin/login.html',}, name='login'),
    url(r'^logout/$', logout_then_login, {'login_url': '/admin/login/'}, name='logout'),
)