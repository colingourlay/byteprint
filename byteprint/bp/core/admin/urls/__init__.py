from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout_then_login

urlpatterns = patterns('bp.core.admin.views',
    (r'^filebrowser/', include('bp.contrib.filebrowser.urls')),
    (r'^settings/', include('bp.core.config.urls.admin')),
    (r'^scraps/', include('bp.core.scraps.urls.admin')),
    (r'^articles/', include('bp.core.articles.urls.admin')),
    url(r'^$',
        'hub',
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
