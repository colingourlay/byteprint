import datetime

from django.shortcuts import get_object_or_404

from bp.core.articles.models import Article
from bp.core.config.models import Setting
from bp.core.scraps.models import Pile, Scrap
from bp.core.scraps import utils as scraps_utils

def article_get(article_id):
    return get_object_or_404(Article, id=article_id)

def article_create(title, author, is_page=False):
    pile = Pile(name="article", is_standalone=False)
    pile.save()
    article = Article(title=title, author=author, pile=pile, is_page=is_page) or None
    article.save()
    pile.name = "article-%d" % article.id
    pile.save()
    scrap = scraps_utils.scrap_create("text-wysiwyg")
    scraps_utils.scrap_repile(scrap.id, pile.id)
    scraps_utils.scrap_toggle(scrap.id, True)
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

def is_scrap_in_article_pile(article_id, scrap_id):
    scrap = scraps_utils.scrap_get(scrap_id)
    article = article_get(article_id)
    if scrap in article.pile.scraps():
        return True
    return False

def article_update_rendered_pile(article_id):
    article = article_get(article_id)
    updated_article_rendered_pile = ""
    for scrap in article.pile.scraps():
        if scrap.is_enabled:
            rendered_scrap, status = scraps_utils.scrap_render(scrap, show_title=False)
            updated_article_rendered_pile += rendered_scrap
    article.rendered_pile = updated_article_rendered_pile
    article.updated = datetime.datetime.now()
    article.save()