from django.shortcuts import get_object_or_404

from platform.core.articles.models import Article
from platform.core.config.models import Setting

def article_get(article_id):
    return get_object_or_404(Article, id=article_id)

def article_create(title, author):
    article = Article(title=title, author=author) or None
    article.save()
    return article

def article_delete(article_id):
    article = article_get(article_id)
    article.delete()

def article_toggle(article_id, status):
    article = article_get(article_id)
    article.is_published = status
    article.save()
    return article