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
    fields = { 'html': forms.CharField(widget=forms.Textarea, initial="<p>Replace this with your HTML</p>") }

    def render(self, widget_data):
        output = widget_data['html']
        return output

class ImageBlueprint(Blueprint):

    name = 'image'
    fields = { 'url': forms.CharField(required=False) }

    def render(self, widget_data):
        output = "<img src=\"" + widget_data['url'] + "\" />"
        return output
        
# class HTMLBlueprint(Blueprint):
# 
#     name = 'html'
#     fields = { 'title': forms.CharField(max_length=40, initial="HTML Widget"),
#         'html': forms.CharField(widget=forms.Textarea, initial="<p>Replace this with your content</p>"),
#         'show_title': forms.BooleanField(required=False, initial=True)}
# 
#     def render(self, widget_data):
#         output = ""
#         if widget_data['show_title']:
#             output += "<h4>" + widget_data['title'] + "</h4>"
#         output += widget_data['html']
#         return output