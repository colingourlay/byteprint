from django.conf.urls.defaults import *

urlpatterns = patterns('bp.core.articles.views',
    url(r'^(?P<slug>[\w-]+)/$',
        'page_detail',
        name='articles_public_page_detail'
    )
)