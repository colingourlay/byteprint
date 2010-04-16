from django.http import Http404
from django.shortcuts import get_object_or_404, redirect

from bp.core.articles import utils
from bp.core.articles.models import Article
from bp.core.public.shortcuts import direct_to_theme

def article_detail(request, article_id=None, year=None, month=None, slug=None):
    if article_id:
        article = utils.article_get(article_id)
        return redirect(
            'articles_public_article_detail',
            year=article.created.year,
            month=article.created.month,
            slug=article.slug
        )
    article = get_object_or_404(
        Article,
        created__year=year,
        created__month=month,
        slug=slug
    )
    if article.is_published:
        return direct_to_theme(
            request,
            'article.html',
            {
                'article': article
            }
        )
    elif request.user == article.author:
        article.title = article.title + " *DRAFT*"
        return direct_to_theme(
            request,
            'article.html',
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
    return direct_to_theme(
        request,
        'archive.html',
        {
            'doc_title': doc_title,
            'articles': articles
        }
    )