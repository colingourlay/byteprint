from datetime import datetime
from xml.etree import ElementTree
from bp.contrib.BeautifulSoup import BeautifulStoneSoup
from bp.core.articles.models import Article
from bp.core.articles import utils as articles_utils
from bp.core.scraps import utils as scraps_utils

# def run(request, xml):
#     tree = ElementTree.fromstring(xml)
#     for item in tree.findall('item'):
#         if item.findtext('wp:status') == 'publish':
#             if item.findtext('wp:post_type') == 'post':
#                 title = item.findtext("title")
#                 author = request.user
#                 article = articles_utils.article_create(title=title, author=author)
#                 article.rendered_pile = item.findtext("content:encoded")
#                 article.is_published = True
#                 created = item.findtext('wp:post_date')
#                 article.created = datetime.strptime(created, "%Y-%m-%d %H:%M:%S")
#                 article.updated = datetime.strptime(created, "%Y-%m-%d %H:%M:%S")
#                 if item.findtext('wp:comment_status') == 'open':
#                     article.enable_comments = True
#                 article.pile.scraps()[0].delete()
#                 scrap = scraps_utils.scrap_create("text-wysiwyg")
#                 scrap_data = scrap.data_load()
#                 scrap_data['content'] = article.rendered_pile
#                 scrap.data_dump(scrap_data)
#                 scrap.title = ""
#                 scrap.is_enabled = True
#                 scrap.save()
#                 scraps_utils.scrap_repile(scrap.id, article.pile.id)
#                 article.save()

def run(request, xml):
    tree = BeautifulStoneSoup(xml)
    for item in tree.findAll('item'):
        if item.find('wp:status').text == 'publish':
            if item.find('wp:post_type').text == 'post':
                title = item.find("title").text
                author = request.user
                article = articles_utils.article_create(title=title, author=author)
                article.rendered_pile = item.find("content:encoded").text
                article.is_published = True
                created = item.find('wp:post_date').text
                article.created = datetime.strptime(created, "%Y-%m-%d %H:%M:%S")
                article.updated = datetime.strptime(created, "%Y-%m-%d %H:%M:%S")
                if item.find('wp:comment_status').text == 'open':
                    article.enable_comments = True
                # article.pile.scraps()[0].delete()
                #                 scrap = scraps_utils.scrap_create("text-wysiwyg")
                #                 scrap_data = scrap.data_load()
                #                 scrap_data['content'] = article.rendered_pile
                #                 scrap.data_dump(scrap_data)
                #                 scrap.title = ""
                #                 scrap.is_enabled = True
                #                 scrap.save()
                #                 scraps_utils.scrap_repile(scrap.id, article.pile.id)
                article.save()