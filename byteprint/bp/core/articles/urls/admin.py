from django.conf.urls.defaults import *

urlpatterns = patterns('bp.core.articles.views.admin',
    url(r'^create/$',
        'article_create',
        name='articles_admin_article_create'
    ),
    url(r'^(?P<article_id>\d+)/delete/$',
        'article_delete',
        name='articles_admin_article_delete'
    ),
    url(r'^(?P<article_id>\d+)/publish/$',
        'article_toggle',
        {'status': True},
        name='articles_admin_article_publish'
    ),
    url(r'^(?P<article_id>\d+)/unpublish/$',
        'article_toggle',
        {'status': False},
        name='articles_admin_article_unpublish'
    ),
    url(r'^(?P<article_id>\d+)/$',
        'article_edit',
        name='articles_admin_article_edit'
    ),
    url(r'^(?P<article_id>\d+)/quickedit/$',
        'articles_manage',
        name='articles_admin_article_quickedit'
    ),
    url(r'^$',
        'articles_manage',
        name='articles_admin_articles_manage'
    ),
    url(r'^(?P<article_id>\d+)/scraps/create/$',
        'article_scrap_create',
        name='articles_admin_article_scrap_create_httppost'
    ),
    url(r'^(?P<article_id>\d+)/scraps/(?P<scrap_id>\d+)/delete/$',
        'article_scrap_delete',
        name='articles_admin_article_scrap_delete'
    ),
    url(r'^(?P<article_id>\d+)/scraps/(?P<scrap_id>\d+)/reposition/(?P<position>\d+)/$',
        'article_scrap_reposition',
        name='articles_admin_article_scrap_reposition'
    ),
    url(r'^(?P<article_id>\d+)/scraps/(?P<scrap_id>\d+)/disable/$',
        'article_scrap_toggle',
        {'status': False},
        name='articles_admin_article_scrap_disable'
    ),
    url(r'^(?P<article_id>\d+)/scraps/(?P<scrap_id>\d+)/enable/$',
        'article_scrap_toggle',
        {'status': True},
        name='articles_admin_article_scrap_enable'
    ),
    url(r'^(?P<article_id>\d+)/scraps/(?P<scrap_id>\d+)/$',
        'article_scrap_edit',
        name='articles_admin_article_scrap_edit'
    ),
)
