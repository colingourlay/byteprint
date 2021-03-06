from django.conf.urls.defaults import *

urlpatterns = patterns('bp.contrib.filebrowser.views',
    
    # filebrowser urls
    url(r'^browse/$', 'browse', name="fb_browse"),
    url(r'^mkdir/', 'mkdir', name="fb_mkdir"),
    url(r'^upload/', 'upload', name="fb_upload"),
    url(r'^rename/$', 'rename', name="fb_rename"),
    url(r'^delete/$', 'delete', name="fb_delete"),
    url(r'^versions/$', 'versions', name="fb_versions"),
    
    url(r'^check_file/$', '_check_file', name="fb_check"),
    url(r'^upload_file/$', '_upload_file', name="fb_do_upload"),
    
)
