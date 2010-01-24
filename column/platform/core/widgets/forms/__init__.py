from django import forms
from django.utils.translation import ugettext_lazy as _
from platform.core.widgets.utils import get_blueprints

BLUEPRINT_CHOICES = get_blueprints(two_tuple=True)

class CreateWidgetForm(forms.Form):
    blueprint_name = forms.ChoiceField(
        choices=BLUEPRINT_CHOICES,
        label='Widget Blueprint',
        help_text="Pick a blueprint from the list and click the Build button",
    )

class CreateGroupForm(forms.Form):
    name = forms.CharField(
        label='Name',
        help_text="The group name is used in your templates to render all of the widgets it contains.",
        max_length=30,
    )

class RenameGroupForm(forms.Form):
    id = forms.CharField(
        max_length=4,
        widget=forms.HiddenInput,
    )
    name = forms.CharField(
        max_length=30,
    )