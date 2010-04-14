from django.conf.urls.defaults import *

urlpatterns = patterns('bp.core.public.views',
    url(r'^$', 'homepage', name='public_homepage'),
    (r'^articles/', include('bp.core.articles.urls')),
)