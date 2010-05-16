from django.conf.urls.defaults import *

urlpatterns = patterns('bp.core.importer.views.admin',
    url(r'^$',
        'import_data',
        name='importer_admin_import_data'
    ),
)