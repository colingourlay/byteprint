from django.http import Http404
from django.shortcuts import get_object_or_404, redirect

from bp.core.articles import utils
from bp.core.articles.models import Article
from bp.core.public.shortcuts import direct_to_theme

ARTICLE_DETAIL_TEMPLATE = 'article.html'
ARTICLE_LIST_TEMPLATE = 'archive.html'
PAGE_DETAIL_TEMPLATE = 'page.html'

def article_detail(request, article_id=None, year=None, month=None, slug=None, template=ARTICLE_DETAIL_TEMPLATE):
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
            template,
            {
                'article': article
            }
        )
    elif request.user == article.author:
        article.title = article.title + " *DRAFT*"
        return direct_to_theme(
            request,
            template,
            {
                'doc_title': article.title,
                'article': article
            }
        )
    else:
        raise Http404

def article_list(request, add_doc_title=True, template=ARTICLE_LIST_TEMPLATE):
    articles = Article.objects.published_articles()
    doc_title = None
    if add_doc_title:
        doc_title = "Archive"
    return direct_to_theme(
        request,
        template,
        {
            'doc_title': doc_title,
            'articles': articles
        }
    )


def page_detail(request, slug=None, template=PAGE_DETAIL_TEMPLATE):
    article = get_object_or_404(
        Article,
        slug=slug,
        is_page=True
    )
    if article.is_published:
        return direct_to_theme(
            request,
            template,
            {
                'page': article
            }
        )
    elif request.user == article.author:
        article.title = article.title + " *DRAFT*"
        return direct_to_theme(
            request,
            template,
            {
                'doc_title': article.title,
                'page': article
            }
        )
    else:
        raise Http404