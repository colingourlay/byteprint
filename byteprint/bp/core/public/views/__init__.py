from django.template import RequestContext

from bp.core.articles.models import Article
from bp.core.articles.views import article_list
from bp.core.public.shortcuts import render_using_theme

def homepage(request):
    return article_list(request, add_doc_title=False)
