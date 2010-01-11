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
    as well as correctly rendering their content.
    """
    __metaclass__ = BlueprintInventory

class TextBlueprint(Blueprint):

    name = 'text'

    def render(self, widget_data):
        return '<p>I am some text</p>'


class ImageBlueprint(Blueprint):

    name = 'image'

    def render(self, widget_data):
        return '<img src="http://www.collider.com/uploads/imageGallery/A_Team/the_a-team_logo.jpg"/>'

class VideoBlueprint(Blueprint):

    name = 'video'

    def render(self, widget_data):
        return '<object width="480" height="295"><param name="movie" value="http://www.youtube.com/v/mh0bLHnmG4M&hl=en_US&fs=1&rel=0&color1=0x3a3a3a&color2=0x999999"></param><param name="allowFullScreen" value="true"></param><param name="allowscriptaccess" value="always"></param><embed src="http://www.youtube.com/v/mh0bLHnmG4M&hl=en_US&fs=1&rel=0&color1=0x3a3a3a&color2=0x999999" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="480" height="295"></embed></object>'
