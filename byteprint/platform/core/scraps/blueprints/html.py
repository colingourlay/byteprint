from django import forms

from platform.core.scraps import Blueprint

class BareHTML(Blueprint):

    name = 'bare-html'
    display_name = 'HTML'
    description = 'This scrap allows you to write bare HTML, which will \
        appear on your site just as you made it.'
    preview = True
    fields = {
        'html': forms.CharField(
            widget = forms.Textarea,
            label = "HTML",
            help_text = "Enter the HTML you want to appear within the scrap. \
                Any valid HTML is permitted, including <script> tags",
            initial = "<p>Replace this with your HTML</p>"
        )
    }

    def render(self, scrap_data):
        output = scrap_data['html']
        return output

class TinyMCEHTML(Blueprint):

    name = 'tinymce-html'
    display_name = 'HTML (TinyMCE)'
    description = 'This scrap enables the TinyMCE WYSIWYG editor for writing \
        HTML as you intend it to look on your site.'
    preview = False
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