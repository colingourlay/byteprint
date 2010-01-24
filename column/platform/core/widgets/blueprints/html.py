from django import forms
from platform.core.widgets import Blueprint

class BareHTML(Blueprint):

    name = 'bare-html'
    display_name = 'HTML'
    description = 'This widget allows you to write bare HTML, which will \
        appear on your site just as you made it.'
    preview = True
    fields = {
        'html': forms.CharField(
            widget = forms.Textarea,
            label = "HTML",
            help_text = "Enter the HTML you want to appear within the widget. \
                Any valid HTML is permitted, including <script> tags",
            initial = "<p>Replace this with your HTML</p>"
        )
    }

    def render(self, widget_data):
        output = widget_data['html']
        return output

class WYSIWYGHTML(Blueprint):

    name = 'wysiwyg-html'
    display_name = 'WYSIWYG HTML'
    description = 'This widget enables a What-You-See-Is-What-You-Get editor \
        for writing HTML as you intend it to look on your site.'
    preview = False
    fields = {
        'html': forms.CharField(
            widget = forms.Textarea(
                attrs = {
                    'id':'wysiwyg_editor'
                }
            ),
            label = "HTML",
            help_text = "Edit the HTML as you want it to appear in   the widget. \
                Any valid HTML is permitted, including <script> tags",
            initial = "<p>Replace this with your HTML</p>"
        )
    }

    def render(self, widget_data):
        output = widget_data['html']
        return output