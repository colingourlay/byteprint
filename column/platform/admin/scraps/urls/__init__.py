from django.conf.urls.defaults import *

urlpatterns = patterns('platform.admin.scraps.views',
    url(r'^blueprints/$',
        'blueprints',
        name='admin_scraps_blueprints'
    ),
    url(r'^piles/create/$',
        'pile_create',
        name='admin_scraps_pile_create'
    ),
    url(r'^piles/(?P<pile_id>\d+)/delete/$',
        'pile_delete',
        name='admin_scraps_pile_delete'
    ),
    url(r'^piles/(?P<pile_id>\d+)/disable/$',
        'pile_toggle',
        {'status': False},
        name='admin_scraps_pile_disable'
    ),
    url(r'^piles/(?P<pile_id>\d+)/enable/$',
        'pile_toggle',
        {'status': True},
        name='admin_scraps_pile_enable'
    ),
    url(r'^piles/(?P<pile_id>\d+)/rename/$',
        'pile_rename',
        name='admin_scraps_pile_rename'
    ),
    url(r'^create/(?P<blueprint_name>([\w-])+)/$',
        'scrap_create',
        name='admin_scraps_scrap_create'
    ),
    url(r'^create/$',
        'scrap_create',
        name='admin_scraps_scrap_create_httppost'
    ),
    url(r'^(?P<scrap_id>\d+)/delete/$',
        'scrap_delete',
        name='admin_scraps_scrap_delete'
    ),
    url(r'^(?P<scrap_id>\d+)/reposition/(?P<position>\d+)/$',
        'scrap_reposition',
        name='admin_scraps_scrap_reposition'
    ),
    url(r'^(?P<scrap_id>\d+)/repile/(?P<pile_id>\d+)/$',
        'scrap_repile',
        name='admin_scraps_scrap_repile'
    ),
    url(r'^(?P<scrap_id>\d+)/unpile/$',
        'scrap_repile',
        name='admin_scraps_scrap_unpile'
    ),
    url(r'^(?P<scrap_id>\d+)/disable/$',
        'scrap_toggle',
        {'status': False},
        name='admin_scraps_scrap_disable'
    ),
    url(r'^(?P<scrap_id>\d+)/enable/$',
        'scrap_toggle',
        {'status': True},
        name='admin_scraps_scrap_enable'
    ),
    url(r'^(?P<scrap_id>\d+)/$',
        'scrap_edit',
        name='admin_scraps_scrap_edit'
    ),
    url(r'^$',
        'manage',
        name='admin_scraps_manage'
    ),
)
