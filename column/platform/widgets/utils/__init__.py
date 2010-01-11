from platform.widgets import Blueprint
from platform.widgets.models import Widget

def get_blueprints(two_tuple=False):
    blueprints = []
    for blueprint in Blueprint.inventory:
        if two_tuple:
            blueprints.append((blueprint.name, blueprint.name))
        else:
            blueprints.append(blueprint.name)
    return blueprints

def get_blueprint(blueprint_name):
    for blueprint in Blueprint.inventory:
        if blueprint.name == blueprint_name:
            return blueprint
    return None

def build_widget(blueprint_name):
    try:
        blueprint = get_blueprint(blueprint_name)
        try:
            widget = Widget(blueprint_name=blueprint_name)
            widget.save()
            return widget, "built widget from blueprint \"" + blueprint_name + "\""
        except:
            return None, "failed to build widget from blueprint \"" + blueprint_name + "\""
    except:
        return None, "the blueprint \"" + blueprint_name + "\" does not exist"
    
def render_widget(widget):
    blueprint = get_blueprint(widget.blueprint_name)
    if blueprint:
        rendered_widget = "<div class=\"widget\">"
        rendered_widget += "<div class=\"widget_header\"><h4>" + widget.blueprint_name + "</h4></div>"
        rendered_widget += "<div class=\"widget_body\">"
        rendered_widget += blueprint().render(widget.data)
        rendered_widget += "</div>"
        rendered_widget += "</div>"
        return rendered_widget
    return ""