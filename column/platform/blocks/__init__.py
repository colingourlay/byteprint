class PluginMount(type):
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            # This branch only executes when processing the mount point itself.
            # So, since this is a new plugin type, not an implementation, this
            # class shouldn't be registered as a plugin. Instead, it sets up a
            # list where plugins can be registered later.
            cls.plugins = []
        else:
            # This must be a plugin implementation, which should be rgistered.
            # Simply appending it to the list is all that's needed to keep
            # track of it later
            cls.plugins.append(cls)

class AbstractPlugin(object):
    """
    Plugins extending this class will be used for creating Block models,
    as well as correctly rendering their content.
    
    create(self, data_dict)
        Recieves a dict containing the data that is needed by the block to
        render the Block's content, and stores it along with the block's
        name, so that the Block instance knows which Plugin can render it.
    """
    __name__ = 'AbstractPlugin'
    __metaclass__ = PluginMount