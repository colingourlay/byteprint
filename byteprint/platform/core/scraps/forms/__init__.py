from django import forms
from django.utils.translation import ugettext_lazy as _

from platform.core.scraps.utils import get_blueprints

BLUEPRINT_CHOICES = get_blueprints(two_tuple=True)

class CreateScrapForm(forms.Form):
    blueprint_name = forms.ChoiceField(
        choices=BLUEPRINT_CHOICES,
        label='',
        help_text="Select a blueprint and click the <strong>Create Scrap</strong> button.",
    )

class CreatePileForm(forms.Form):
    name = forms.CharField(
        label='',
        help_text="Enter a name and click the <strong>Create Pile</strong> button.",
        max_length=30,
    )

class RenamePileForm(forms.Form):
    name = forms.CharField(
        max_length=30,
    )