from django import forms

class BlueprintInventory(type):
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'inventory'):
            # This branch only executes when processing the mount point itself.
            # So, since this is a new blueprint type, not an implementation,
            # this class shouldn't be registered as a Blueprint. Instead, it
            # sets up a list where blueprints can be registered later.
            cls.inventory = []
        else:
            # This must be a blueprint implementation, which should be
            # registered. Simply appending it to the list is all that's needed
            # to keep track of it later
            cls.inventory.append(cls)

class Blueprint(object):
    """
    Blueprints extending this class will be used for creating Widget models,
    as well as rendering their content.
    """
    __metaclass__ = BlueprintInventory

class HTMLBlueprint(Blueprint):

    name = 'html'
    fields = {
        'html': forms.CharField(
            widget = forms.Textarea,
            label = "HTML",
            help_text = "Enter the HTML you want to appear within the widget. \
                Any valid HTML is permitted, including <script> tags",
            initial="<p>Replace this with your HTML</p>"
        )
    }

    def render(self, widget_data):
        output = widget_data['html']
        return output

class ImageBlueprint(Blueprint):

    name = 'image'
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

class SyntaxBlueprint(Blueprint):
    
    name = 'syntax'
    fields = {
        'syntax': forms.CharField(
            widget = forms.Textarea(
                attrs = {
                    'id':'syntax_editor'
                }
            ),
            label = "Syntax",
            help_text = "Enter the syntax you want to appear within the widget",
            initial = "print \"Hello World\";"
        )
    }

    def render(self, widget_data):
        output = "<pre><code>" + widget_data['syntax'] + "</code></pre>"
        return output