from django import forms

from bp.core.scraps import Blueprint

class SampleBlueprint(Blueprint):

    name = 'sample-blueprint'
    family = 'Sample'
    display_name = 'Blueprint'
    description = 'Sample Description'
    preview = True
    fields = {
        'sample_field': forms.CharField(
            label = "Sample Field",
            help_text = "Sample Help Text",
            initial = "Sample Content"
        )
    }

    def render(self, scrap_data):
        output = scrap_data['sample_field']
        return output