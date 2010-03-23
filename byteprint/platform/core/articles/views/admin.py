from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from platform.core.articles.forms import CreateArticleForm, QuickEditArticleForm
from platform.core.articles.models import Article
from platform.core.articles import utils

ARTICLE_EDIT_TEMPLATE = 'articles/admin/article_edit.html'

@login_required
def articles_manage(request, article_id=None):
    articles = Article.objects.all()
    create_article_form = CreateArticleForm()
    quick_edit_article = None
    quick_edit_article_form = None
    if article_id:
        quick_edit_article = utils.article_get(article_id)
        data = {
            'title': quick_edit_article.title,
            'published': quick_edit_article.published,
            'publish': quick_edit_article.publish,
            'published': quick_edit_article.published,
            'show_comments': quick_edit_article.show_comments,
            'enable_comments': quick_edit_article.enable_comments
        }
        quick_edit_article_form = QuickEditArticleForm(data)
        if request.method == 'POST':
            quick_edit_article_form = QuickEditArticleForm(request.POST)
            if quick_edit_article_form.is_valid():
                quick_edit_article.title = quick_edit_article_form.cleaned_data['title']
                quick_edit_article.published = quick_edit_article_form.cleaned_data['published']
                quick_edit_article.publish = quick_edit_article_form.cleaned_data['publish']
                quick_edit_article.show_comments = quick_edit_article_form.cleaned_data['show_comments']
                quick_edit_article.enable_comments = quick_edit_article_form.cleaned_data['enable_comments']
                quick_edit_article.save()
                return redirect('articles_admin_articles_manage')
    return render_to_response(
        'articles/admin/articles_manage.html', {
            'menu_current': 'content_articles',
            'h1': 'Manage Articles',
            'articles': articles,
            'create_article_form': create_article_form,
            'quick_edit_article': quick_edit_article,
            'quick_edit_article_form': quick_edit_article_form
        },
        RequestContext(request)
    )

@login_required
def article_create(request):
    if request.method == 'POST':
        article_create_form = CreateArticleForm(request.POST)
        if article_create_form.is_valid():
            article_title = article_create_form.cleaned_data['title']
            article = utils.article_create(title=article_title, author=request.user)
    return redirect('articles_admin_articles_manage')

@login_required
def article_delete(request, article_id):
    utils.article_delete(article_id)
    return redirect('articles_admin_articles_manage')

@login_required
def article_edit(request, article_id, template=ARTICLE_EDIT_TEMPLATE):
    article = utils.article_get(article_id)
    msg = None
    if request.method == 'POST':
        pass
    h1 = "Editing \"" + article.title + "\""
    return render_to_response(
        template, {
            'menu_current': 'content_articles',
            'h1': h1,
            'article': article,
            'msg': msg
        },
        RequestContext(request)
    )