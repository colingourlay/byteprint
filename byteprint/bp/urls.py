from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^installation/', include('bp.core.installation.urls')),
    (r'^admin/', include('bp.core.admin.urls')),
    (r'^', include('bp.core.public.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_DIR, 'show_indexes':True}
        ),
    )