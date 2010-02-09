from django import forms
from django.utils.translation import ugettext_lazy as _
from platform.core.scraps.utils import get_blueprints

BLUEPRINT_CHOICES = get_blueprints(two_tuple=True)

class CreateScrapForm(forms.Form):
    blueprint_name = forms.ChoiceField(
        choices=BLUEPRINT_CHOICES,
        label='Scrap Blueprint',
    )

class CreatePileForm(forms.Form):
    name = forms.CharField(
        label='Name',
        help_text="The pile name is used in your templates to render all of the scraps it contains.",
        max_length=30,
    )

class RenamePileForm(forms.Form):
    name = forms.CharField(
        max_length=30,
    )