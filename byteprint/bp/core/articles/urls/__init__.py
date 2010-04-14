from django.conf.urls.defaults import *

urlpatterns = patterns('bp.core.articles.views',
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w-]+)/$',
        'article_detail',
        name='articles_public_article_detail'
    ),
    url(r'^(?P<article_id>\d+)/$',
        'article_detail',
        name='articles_public_article_detail_id'
    ),
    url(r'^$',
        'article_list',
        name='articles_public_article_list'
    ),
)