from django import forms

from bp.core.importer import IMPORT_SOURCE_CHOICES

class ImportDataForm(forms.Form):
    import_source = forms.ChoiceField(
        choices = IMPORT_SOURCE_CHOICES,
        label = "Import Source",
        help_text = "Select the type of blog you are importing from."
    )
    import_data_file = forms.FileField(
        label = "Import Data",
        help_text = "Select the file you exported from your current blog."
    )