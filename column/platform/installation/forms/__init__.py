from django import forms
from django.utils.translation import ugettext_lazy as _

class InstallationForm(forms.Form):
    site_title = forms.CharField(
        max_length=140,
        label='Site Title',
        help_text="The title of your published site. You can change this later.",
        initial="My Site",
    )
    username = forms.CharField(
        max_length=30,
        label='Username',
        help_text="You will use this to log into the byteprint admin site.",
    )
    password = forms.CharField(
        max_length=128,
        label='Password',
        help_text="Try to use a mixture of upper/lower case letters and numbers.",
        widget=forms.PasswordInput,
    )
    password_confirm = forms.CharField(
        max_length=128,
        label='Repeat Password',
        help_text="Both passwords must match in order to create your user account.",
        widget=forms.PasswordInput,
    )
    email = forms.EmailField(
        label='Email',
        help_text="You email address is used for admin notifications, or if you forget your login details.",
    )
    
    def clean(self):
        if 'password' in self.cleaned_data and 'password_confirm' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
                raise forms.ValidationError(_("Both password fields must match."))
        return self.cleaned_data
    
