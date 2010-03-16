from django import forms

class GeneralSettingsForm(forms.Form):
    site_title = forms.CharField(
        max_length=140,
        label='Site Title',
        help_text='The title of your published site (usually displayed in the \
            site header).',
    )
    site_subtitle = forms.CharField(
        label='Site Subtitle',
        help_text='A summary of what your site is about.',
    )
    site_email = forms.EmailField(
        label='Site Email',
        help_text='This email address is used for site notifications, and is \
            usually the email address of the admin user.',
    )

class ScrapsSettingsForm(forms.Form):
    scrap_div_class = forms.CharField(
        max_length=40,
        label='Scrap <div> Element Classes',
        help_text='Each scrap on your site is rendered inside a <div> element.\
            Enter the css classes you would like to appear on these elements \
            to aid your page styling.',
    )