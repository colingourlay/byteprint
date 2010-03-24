from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from platform.core.articles.forms import CreateArticleForm

@login_required
def dashboard(request):
    
    create_article_form = CreateArticleForm()
    
    return render_to_response(
        'admin/dashboard.html',
        {
            'h1': 'Dashboard',
            'create_article_form': create_article_form
        },
        RequestContext(request)
    )