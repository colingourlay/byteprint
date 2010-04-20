from django.conf.urls.defaults import *

urlpatterns = patterns('bp.core.articles.views.admin',
    url(r'^create/$',
        'article_create', {'is_page': True},
        name='articles_admin_page_create'
    ),
    url(r'^(?P<article_id>\d+)/delete/$',
        'article_delete', {'is_page': True},
        name='articles_admin_page_delete'
    ),
    url(r'^(?P<article_id>\d+)/publish/$',
        'article_toggle',
        {'status': True, 'is_page': True},
        name='articles_admin_page_publish'
    ),
    url(r'^(?P<article_id>\d+)/unpublish/$',
        'article_toggle',
        {'status': False, 'is_page': True},
        name='articles_admin_page_unpublish'
    ),
    url(r'^(?P<article_id>\d+)/$',
        'article_edit', {'is_page': True},
        name='articles_admin_page_edit'
    ),
    url(r'^(?P<article_id>\d+)/quickedit/$',
        'articles_manage', {'is_page': True},
        name='articles_admin_page_quickedit'
    ),
    url(r'^$',
        'articles_manage', {'is_page': True},
        name='articles_admin_pages_manage'
    ),
    url(r'^(?P<article_id>\d+)/scraps/create/$',
        'article_scrap_create', {'is_page': True},
        name='articles_admin_page_scrap_create_httppost'
    ),
    url(r'^(?P<article_id>\d+)/scraps/(?P<scrap_id>\d+)/delete/$',
        'article_scrap_delete', {'is_page': True},
        name='articles_admin_page_scrap_delete'
    ),
    url(r'^(?P<article_id>\d+)/scraps/(?P<scrap_id>\d+)/reposition/(?P<position>\d+)/$',
        'article_scrap_reposition', {'is_page': True},
        name='articles_admin_page_scrap_reposition'
    ),
    url(r'^(?P<article_id>\d+)/scraps/(?P<scrap_id>\d+)/disable/$',
        'article_scrap_toggle',
        {'status': False, 'is_page': True},
        name='articles_admin_page_scrap_disable'
    ),
    url(r'^(?P<article_id>\d+)/scraps/(?P<scrap_id>\d+)/enable/$',
        'article_scrap_toggle',
        {'status': True, 'is_page': True},
        name='articles_admin_page_scrap_enable'
    ),
    url(r'^(?P<article_id>\d+)/scraps/(?P<scrap_id>\d+)/$',
        'article_scrap_edit', {'is_page': True},
        name='articles_admin_page_scrap_edit'
    ),
)
