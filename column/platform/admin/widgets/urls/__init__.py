from django.conf.urls.defaults import *

urlpatterns = patterns('platform.admin.widgets.views',
    url(r'^blueprints/$',
        'blueprints',
        name='admin_widgets_blueprints'
    ),
    url(r'^groups/create/$',
        'group_create',
        name='admin_widgets_group_create'
    ),
    url(r'^groups/(?P<group_id>\d+)/delete/$',
        'group_delete',
        name='admin_widgets_group_delete'
    ),
    url(r'^groups/(?P<group_id>\d+)/disable/$',
        'group_toggle',
        {'status': False},
        name='admin_widgets_group_disable'
    ),
    url(r'^groups/(?P<group_id>\d+)/enable/$',
        'group_toggle',
        {'status': True},
        name='admin_widgets_group_enable'
    ),
    url(r'^groups/(?P<group_id>\d+)/rename/$',
        'group_rename',
        name='admin_widgets_group_rename'
    ),
    url(r'^create/(?P<blueprint_name>([\w-])+)/$',
        'widget_create',
        name='admin_widgets_widget_create'
    ),
    url(r'^create/$',
        'widget_create',
        name='admin_widgets_widget_create_httppost'
    ),
    url(r'^(?P<widget_id>\d+)/delete/$',
        'widget_delete',
        name='admin_widgets_widget_delete'
    ),
    url(r'^(?P<widget_id>\d+)/reposition/(?P<position>\d+)/$',
        'widget_reposition',
        name='admin_widgets_widget_reposition'
    ),
    url(r'^(?P<widget_id>\d+)/regroup/(?P<group_id>\d+)/$',
        'widget_regroup',
        name='admin_widgets_widget_regroup'
    ),
    url(r'^(?P<widget_id>\d+)/ungroup/$',
        'widget_regroup',
        name='admin_widgets_widget_ungroup'
    ),
    url(r'^(?P<widget_id>\d+)/disable/$',
        'widget_toggle',
        {'status': False},
        name='admin_widgets_widget_disable'
    ),
    url(r'^(?P<widget_id>\d+)/enable/$',
        'widget_toggle',
        {'status': True},
        name='admin_widgets_widget_enable'
    ),
    url(r'^(?P<widget_id>\d+)/$',
        'widget_edit',
        name='admin_widgets_widget_edit'
    ),
    url(r'^$',
        'manage',
        name='admin_widgets_manage'
    ),
)
