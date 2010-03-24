from django.template import RequestContext

from platform.core.articles.models import Article
from platform.core.articles.views import article_list
from platform.core.public.shortcuts import render_using_theme

def homepage(request):
    return article_list(request, add_doc_title=False)
