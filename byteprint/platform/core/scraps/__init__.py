import re

from django import forms
from django.template import add_to_builtins

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
    Blueprints extending this class will be used for creating scrap models,
    as well as rendering their content.
    """
    __metaclass__ = BlueprintInventory

from blueprints import *

add_to_builtins('platform.core.scraps.templatetags.scraps')