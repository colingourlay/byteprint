from platform.widgets import Blueprint
from platform.widgets.models import Widget

def get_blueprint(blueprint_name):
    for blueprint in Blueprint.inventory:
        if blueprint.name == blueprint_name:
            return blueprint
    return None

def build_widget(blueprint_name):    
    print 'building ' + blueprint_name + ' widget...'
    try:
        blueprint = get_blueprint(blueprint_name)
        print '...match found...'
        try:
            widget = Widget(blueprint_name=blueprint_name)
            widget.save()
            print '...ok'
            return widget, "built widget from blueprint \"" + blueprint_name + "\""
        except:
            print '...failed:'
            return None, "failed to build widget from blueprint \"" + blueprint_name + "\""
    except:
        print '...not a blueprint'
        return None, "the blueprint \"" + blueprint_name + "\" does not exist"

#use this method for rendering of forms and content        
#widget = blueprint().render()