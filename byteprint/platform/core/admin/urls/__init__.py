from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout_then_login

urlpatterns = patterns('platform.core.admin.views',
    (r'^settings/', include('platform.core.config.urls.admin')),
    (r'^scraps/', include('platform.core.scraps.urls.admin')),
    (r'^articles/', include('platform.core.articles.urls.admin')),
    url(r'^$',
        'dashboard',
        name='admin'
    ),
    url(r'^login/$',
        login,
        {'template_name': 'admin/login.html'},
        name='login'
    ),
    url(r'^logout/$',
        logout_then_login,
        {'login_url': '/admin/login/'},
        name='logout'
    ),
)
