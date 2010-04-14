from django import forms
from django.template.defaultfilters import date

from bp.core.articles.models import Article
from bp.core.scraps import Blueprint

class ArticlesLatestArticles(Blueprint):

    name = 'articles-latest-articles'
    family = 'Articles'
    display_name = 'Latest Articles'
    description = 'This scrap will display the latest articles to be published \
        on your site. You can choose how many are displayed.'
    preview = True
    fields = {
        'number': forms.IntegerField(
            required = False,
            min_value = 1,
            label = "Number of Articles",
            help_text = "Enter the number of articles you would like to be \
                displayed. If you leave this blank, 5 articles will be shown \
                by default."
        ),
        'show_dates': forms.BooleanField(
            required = False,
            initial = False,
            label = "Show Dates",
            help_text = "If you check this box, the article's original \
                publication date will be displayed alongside its title."
        )
    }

    def render(self, scrap_data):
        number = scrap_data['number'] or 5
        articles = Article.objects.latest(number)
        output = "<ul>"
        for article in articles:
            output += "<li>"
            output += "<a href=\"" + article.get_absolute_url() + "\">"
            output += article.title
            output += "</a>"
            if 'show_dates' in scrap_data:
                output += " <span>("
                output += date(article.created, "d M Y")
                output += ")</span>"
            output += "</li>"
        output += "</ul>"
        return output