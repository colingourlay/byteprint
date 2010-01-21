from django import forms
from platform.core.widgets import Blueprint

class ImageFromURL(Blueprint):

    name = 'image-from-url'
    display_name = 'Image (from URL)'
    preview = True
    fields = {
        'url': forms.CharField(
            required = False,
            label = "Image URL",
            help_text = "Enter the URL of an image resource. This will be \
                built into an image tag and placed inside the widget."
        ),
        'alt': forms.CharField(
            required = False,
            label = "Image Alternative Text",
            help_text = "This appears instead of the image when your visitors \
                cannot view images."
        ),
        'title': forms.CharField(
            required = False,
            label = "Image Title",
            help_text = "The image's title. This appears as a tooltip when \
                visitors hover over your image."
        )
    }

    def render(self, widget_data):
        output = "<img src=\"" + widget_data['url'] + "\" alt=\"" + \
            widget_data['alt'] + "\" title=\"" + widget_data['title'] + "\"/>"
        return output