from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
#    (r'^blocks/', include('platform.blocks.urls')),
    (r'^admin/', include('platform.admin.urls')),
    (r'^', include('platform.core.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^content/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.CONTENT_DIR, 'show_indexes':True}
		),
	)