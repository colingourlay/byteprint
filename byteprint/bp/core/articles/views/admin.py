from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from bp.core.articles.forms import CreateArticleForm, QuickEditArticleForm
from bp.core.articles.models import Article
from bp.core.articles import utils
from bp.core.scraps import utils as scraps_utils
from bp.core.scraps.forms import CreateScrapForm

ARTICLE_EDIT_TEMPLATE = 'articles/admin/article_edit.html'
ARTICLE_SCRAP_EDIT_TEMPLATE = 'articles/admin/article_scrap_edit.html'

@login_required
def articles_manage(request, article_id=None):
    articles = Article.objects.all().order_by('-created')
    create_article_form = CreateArticleForm()
    quick_edit_article = None
    quick_edit_article_form = None
    if article_id:
        quick_edit_article = utils.article_get(article_id)
        data = {
            'title': quick_edit_article.title,
            'is_published': quick_edit_article.is_published,
            'show_comments': quick_edit_article.show_comments,
            'enable_comments': quick_edit_article.enable_comments
        }
        quick_edit_article_form = QuickEditArticleForm(data)
        if request.method == 'POST':
            quick_edit_article_form = QuickEditArticleForm(request.POST)
            if quick_edit_article_form.is_valid():
                quick_edit_article.title = quick_edit_article_form.cleaned_data['title']
                quick_edit_article.is_published = quick_edit_article_form.cleaned_data['is_published']
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
def article_toggle(request, article_id, status):
    article = utils.article_toggle(article_id, status)
    return redirect('articles_admin_articles_manage')

@login_required
def article_edit(request, article_id, template=ARTICLE_EDIT_TEMPLATE):
    article = utils.article_get(article_id)
    create_scrap_form = CreateScrapForm()
    msg = None
    if request.method == 'POST':
        pass
    h1 = "Editing \"" + article.title + "\""
    return render_to_response(
        template, {
            'menu_current': 'content_articles',
            'h1': h1,
            'article': article,
            'create_scrap_form': create_scrap_form,
            'msg': msg
        },
        RequestContext(request)
    )

@login_required
def article_scrap_create(request, article_id):
    if request.method == 'POST':
        article = utils.article_get(article_id)
        create_scrap_form = CreateScrapForm(request.POST)
        if create_scrap_form.is_valid():
            blueprint_name = create_scrap_form.cleaned_data['blueprint_name']
            scrap = scraps_utils.scrap_create(blueprint_name)
            scraps_utils.scrap_repile(scrap.id, article.pile.id)
    return redirect('articles_admin_article_edit', article_id=article_id)

# TODO : Still to implement post & form logic
@login_required
def article_scrap_edit(request, article_id, scrap_id, template=ARTICLE_SCRAP_EDIT_TEMPLATE):
    article = utils.article_get(article_id)
    scrap = scraps_utils.scrap_get(scrap_id)
    msg = None
    if request.method == 'POST':
        # only update upon save after post    
        scrap_edit_form = scraps_utils.scrap_get_edit_form(scrap, False)
        scrap_edit_form = scrap_edit_form(request.POST)
        if scrap_edit_form.is_valid():
            scraps_utils.scrap_update(scrap, request.POST)
            utils.article_update_rendered_pile(article_id)
            msg = 'Your changes to this ' + scrap.blueprint_display_name() \
                + ' scrap were saved'
            return redirect('articles_admin_article_edit', article_id=article_id)
    else:
        scrap_edit_form = scraps_utils.scrap_edit_form_instance(scrap, False)
    h1 = "Editing \"" + article.title + "\""
    return render_to_response(
        template, {
            'menu_current': 'content_articles',
            'h1': h1,
            'article': article,
            'editable_scrap': scrap,
            'scrap_edit_form': scrap_edit_form,
            'msg': msg
        },
        RequestContext(request)
    )
    
@login_required
def article_scrap_delete(request, article_id, scrap_id):
    if utils.is_scrap_in_article_pile(article_id, scrap_id):
        scraps_utils.scrap_delete(scrap_id)
    utils.article_update_rendered_pile(article_id)
    return redirect('articles_admin_article_edit', article_id=article_id)

@login_required
def article_scrap_toggle(request, article_id, scrap_id, status):
    scraps_utils.scrap_toggle(scrap_id, status)
    utils.article_update_rendered_pile(article_id)
    return redirect('articles_admin_article_edit', article_id=article_id)

@login_required
def article_scrap_reposition(request, article_id, scrap_id, position):
    scraps_utils.scrap_reposition(scrap_id, position)
    utils.article_update_rendered_pile(article_id)
    return redirect('articles_admin_article_edit', article_id=article_id)