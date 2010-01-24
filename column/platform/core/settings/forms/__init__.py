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

class WidgetsSettingsForm(forms.Form):
    widget_div_class = forms.CharField(
        max_length=40,
        label='Widget <div> Element Classes',
        help_text='Each widget on your site is rendered inside a <div> element.\
            Enter the css classes you would like to appear on these elements \
            to aid your page styling.',
    )