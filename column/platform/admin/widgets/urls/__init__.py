from django.conf.urls.defaults import *

urlpatterns = patterns('platform.admin.widgets.views',
    url(r'^groups/add/$',
        'add_group',
        name='admin_widgets_add_group'
    ),
    url(r'^groups/(?P<group_id>\d+)/delete/$',
        'delete_group',
        name='admin_widgets_delete_group'
    ),
    url(r'^build/$',
        'build',
        name='admin_widgets_build'
    ),
    url(r'^(?P<widget_id>\d+)/delete/$',
        'delete',
        name='admin_widgets_delete'
    ),
    url(r'^(?P<widget_id>\d+)/reposition/(?P<position>\d+)/$',
        'reposition',
        name='admin_widgets_reposition'
    ),
    url(r'^(?P<widget_id>\d+)/regroup/(?P<group_id>\d+)/$',
        'regroup',
        name='admin_widgets_regroup'
    ),
    url(r'^(?P<widget_id>\d+)/ungroup/$',
        'regroup',
        name='admin_widgets_ungroup'
    ),
    url(r'^(?P<widget_id>\d+)/disable/$',
        'toggle',
        {'status': False},
        name='admin_widgets_disable'
    ),
    url(r'^(?P<widget_id>\d+)/enable/$',
        'toggle',
        {'status': True},
        name='admin_widgets_enable'
    ),
    url(r'^(?P<widget_id>\d+)/$',
        'edit',
        name='admin_widgets_edit'
    ),
    url(r'^$',
        'manage',
        name='admin_widgets_manage'
    ),
)
