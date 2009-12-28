from django import forms
from django.contrib.auth.models import User
from django.forms.util import ErrorList

class InstallationForm(forms.Form):
    blog_title = forms.CharField(
        max_length=140,
        label='Blog Title',
    )
    username = forms.CharField(
        max_length=30,
        label='Username',
    )
    password = forms.CharField(
        max_length=128,
        label='Password',
        widget=forms.PasswordInput,
    )
    password_confirm = forms.CharField(
        max_length=128,
        label='Confirm Password',
        widget=forms.PasswordInput,
    )
    email = forms.EmailField(
        label='Email',
    )