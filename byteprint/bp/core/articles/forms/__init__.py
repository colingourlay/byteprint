from django import forms

class CreateArticleForm(forms.Form):
    title = forms.CharField(
        max_length=140,
        label='',
        help_text='Enter a title for your new article, and click the <strong>Create Article</strong> button to start editing.'
    )
    
class QuickEditArticleForm(forms.Form):
    title = forms.CharField(
        max_length=140,
        label='Title',
        help_text='When you change the title of this article, a new slug will be generated automatically.'
    )
    is_published = forms.BooleanField(
        label='Publish',
        required=False
    )
    show_comments = forms.BooleanField(
        label='Show Existing Comments',
        required=False
    )
    enable_comments = forms.BooleanField(
        label='Accept New Comments',
        required=False
    )