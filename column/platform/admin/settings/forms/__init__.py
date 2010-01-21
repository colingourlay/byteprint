from django import forms

class GeneralSettingsForm(forms.Form):
    blog_title = forms.CharField(
        max_length=140,
        label='Blog Title',
        help_text='The title of your published blog (usually displayed in the \
            site header).',
    )
    blog_subtitle = forms.CharField(
        label='Blog Subtitle',
        help_text='A summary of what your blog is about.',
    )
    admin_email = forms.EmailField(
        label='Admin Email',
        help_text='You email address is used for admin notifications, or if \
            you forget your login details.',
    )