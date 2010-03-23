from django.conf.urls.defaults import *

urlpatterns = patterns('platform.core.articles.views.admin',
    url(r'^create/$',
        'article_create',
        name='articles_admin_article_create'
    ),
    url(r'^(?P<article_id>\d+)/delete/$',
        'article_delete',
        name='articles_admin_article_delete'
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
)
