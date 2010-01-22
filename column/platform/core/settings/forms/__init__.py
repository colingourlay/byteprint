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
        label='Widget <div> Class',
        help_text='Widgets are each rendered inside a <div> with a css class \
            which allows you to add general styling to them. This field \
            defines the class that is attributed to all of your widgets.',
    )