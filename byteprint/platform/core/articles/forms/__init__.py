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
    published = forms.DateTimeField(
        label='Publication Date',
        help_text='Your article will be published on this date if you have also checked the <strong>Publish</strong> checkbox.'
    )
    publish = forms.BooleanField(
        label='Publish',
        help_text='Your article will be published unless the <strong>Publication Date</strong> is in the future.',
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