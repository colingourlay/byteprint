from django import forms

from platform.core.scraps import Blueprint
from platform.contrib.django_markup.markup import formatter

class HTML(Blueprint):

    name = 'text-html'
    family = 'Text'
    display_name = 'HTML'
    description = 'This scrap allows you to write bare HTML, which will \
        be rendered just as it was written. Any valid HTML is permitted, \
        including &lt;script&gt; tags'
    preview = True
    fields = {
        'html': forms.CharField(
            widget = forms.Textarea(
                attrs = {
                    'class':'monospaced'
                }
            ),
            label = "HTML",
            help_text = "Enter the HTML you want to appear within the scrap. \
                Any valid HTML is permitted, including &lt;script&gt; tags",
            initial = "<p>Replace this with your HTML</p>"
        ),
        'language': forms.CharField(
            widget = forms.HiddenInput,
            label = "",
            initial = "html",
            required = False
        )
    }

    def render(self, scrap_data):
        output = scrap_data['html']
        return output

class WYSIWYG(Blueprint):

    name = 'text-wysiwyg'
    family = 'Text'
    display_name = 'WYSIWYG'
    description = 'This scrap enables the TinyMCE WYSIWYG editor for writing \
        HTML as you intend it to look on your site.'
    fields = {
        'content': forms.CharField(
            widget = forms.Textarea(
                attrs = {
                    'cols': 80,
                    'rows': 40
                }
            ),
            label = "Content",
            required = False
        )
    }

    def render(self, scrap_data):
        output = scrap_data['content']
        return output

class FilteredMarkup(Blueprint):

    name = 'text-markup-filter'
    family = 'Text'
    display_name = 'Filtered Markup'
    description = 'This scrap allows you to write text which will be passed \
        through a markup filter of your choice and rendered as HTML. Note: you \
        must install dependencies for each filter you wish to use.'
    preview = True
    fields = {
        'markup': forms.CharField(
            widget = forms.Textarea,
            label = "Markup",
            initial = "Replace this with your markup"
        ),        
        'filter': forms.ChoiceField(
            label = "Markup Filter",
            help_text = "Choose a filter to by applied to your markup.",
            choices = formatter.choices(),
            initial = "none"
        )
    }

    def render(self, scrap_data):
        output = ""
        try:
            output += formatter(
                scrap_data['markup'],
                filter_name=scrap_data['filter']
            )
        except ImportError:
            output += "<!-- Cannot render HTML: '" + scrap_data['filter'] + \
                "' not found. -->"