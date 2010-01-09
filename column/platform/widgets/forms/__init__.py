from django import forms
from django.utils.translation import ugettext_lazy as _
from platform.widgets.utils import get_blueprints

BLUEPRINT_CHOICES = get_blueprints(two_tuple=True)

class BuildWidgetForm(forms.Form):
    blueprint_name = forms.ChoiceField(
        choices=BLUEPRINT_CHOICES,
        label='Blueprint',
        help_text="Pick a blueprint from the list to build a widget from",
    )
