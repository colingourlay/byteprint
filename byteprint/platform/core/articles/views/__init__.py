from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.template import RequestContext

from platform.core.articles import utils
from platform.core.articles.models import Article
from platform.core.public.shortcuts import render_using_theme

def article_detail(request, article_id=None, year=None, month=None, slug=None):
    if article_id:
        article = utils.article_get(article_id)
        return redirect('articles_public_article_detail', year=article.created.year, month=article.created.month, slug=article.slug)
    article = get_object_or_404(Article, created__year=year, created__month=month, slug=slug)
    if article.is_published:
        return render_using_theme('article.html', RequestContext(request), {'article': article})
    elif request.user == article.author:
        article.title = "[DRAFT] " + article.title
        return render_using_theme(
            'article.html',
            RequestContext(request),
            {
                'doc_title': article.title,
                'article': article
            }
        )
    else:
        raise Http404

def article_list(request, add_doc_title=True):
    articles = Article.objects.are_published()
    doc_title = None
    if add_doc_title:
        doc_title = "Archive"
    return render_using_theme(
        'archive.html',
        RequestContext(request),
        {
            'doc_title': doc_title,
            'articles': articles
        }
    )