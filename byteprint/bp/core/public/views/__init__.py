from bp.core.articles.views import article_list

def homepage(request):
    return article_list(request, add_doc_title=False)
