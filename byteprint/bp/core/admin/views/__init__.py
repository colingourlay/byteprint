from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template

from bp.core.articles.forms import CreateArticleForm

HUB_TEMPLATE = 'admin/hub.html'

@login_required
def hub(request, template=HUB_TEMPLATE):
    
    create_article_form = CreateArticleForm()
    
    return direct_to_template(
        request,
        template,
        {
            'h1': 'The Hub',
            'create_article_form': create_article_form
        }
    )