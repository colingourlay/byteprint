from django.shortcuts import get_object_or_404

from platform.core.articles.models import Article
from platform.core.config.models import Setting
from platform.core.scraps.models import Pile

def article_get(article_id):
    return get_object_or_404(Article, id=article_id)

def article_create(title, author):
    pile = Pile(name="article", is_standalone=False)
    pile.save()
    article = Article(title=title, author=author, pile=pile) or None
    article.save()
    return article

def article_delete(article_id):
    article = article_get(article_id)
    article.pile.delete()
    article.delete()

def article_toggle(article_id, status):
    article = article_get(article_id)
    article.is_published = status
    article.save()
    return article