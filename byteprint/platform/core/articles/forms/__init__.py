from django import forms

class CreateArticleForm(forms.Form):
    title = forms.CharField(
        max_length=140,
        label='Article Title'
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
        help_text='Your article will be published if the <strong>Publication Date</strong> is not in the future.',
        required=False
    )
    show_comments = forms.BooleanField(
        label='Show Comments',
        required=False
    )
    enable_comments = forms.BooleanField(
        label='Show Comment Form',
        required=False
    )