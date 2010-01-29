from django import forms
from django.shortcuts import get_object_or_404
from platform.core.widgets import Blueprint
from platform.core.widgets.models import Group, Widget

def get_blueprints(two_tuple=False):
    blueprints = []
    for blueprint in Blueprint.inventory:
        if two_tuple:
            blueprints.append((blueprint.name, blueprint.display_name))
        else:
            blueprints.append(blueprint.name)
    return blueprints

def get_blueprint(blueprint_name):
    for blueprint in Blueprint.inventory:
        if blueprint.name == blueprint_name:
            return blueprint
    return None

def group_get(group_id):
    return get_object_or_404(Group, id=group_id)

def group_delete(group_id):
    group = group_get(group_id)
    widgets = group.widgets()
    for widget in widgets:
        widget.group = None
        widget.group_position = 0
        widget.save()
    group.delete()

def widget_create(blueprint_name):
    try:
        blueprint = get_blueprint(blueprint_name)
        try:
            widget_data = {}
            for key, value in blueprint.fields.items():
                widget_data[key] = value.initial or ""
            widget = Widget(blueprint_name=blueprint_name, data="")
            widget.data_dump(widget_data)
            widget.save()
            return widget
        except:
            return None
    except:
        return None
        
def widget_get(widget_id):
    return get_object_or_404(Widget, id=widget_id)

def widget_update(widget, data):
    widget.data_dump(data)
    widget.save()

def widget_get_edit_form(widget):
    blueprint = get_blueprint(widget.blueprint_name)
    return type('EditWidgetForm', (forms.BaseForm,), { 'base_fields': blueprint.fields})

def widget_edit_form_instance(widget):
    edit_widget_form_class = widget_get_edit_form(widget)
    widget_data = widget.data_load()
    return edit_widget_form_class(widget_data)

def widget_delete(widget_id):
    widget = get_object_or_404(Widget, id=widget_id)
    widget_regroup(widget_id, None)
    widget.delete()

def widget_has_preview(widget):
    blueprint = get_blueprint(widget.blueprint_name)
    try:
        return blueprint.preview
    except:
        return False

def widget_render(widget):
    blueprint = get_blueprint(widget.blueprint_name)
    if blueprint:
        try:
            return blueprint().render(widget.data_load()), True
        except:
            return "<!-- " + blueprint.display_name + " failed to render -->", False
    return "<!-- " + widget.blueprint_name + " is not a blueprint -->", False

def widget_toggle(widget_id, status):
    widget = get_object_or_404(Widget, id=widget_id)
    widget.is_enabled = status
    widget.save()

def widget_regroup(widget_id, group_id):
    widget = get_object_or_404(Widget, id=widget_id)
    group_to_move_to = None
    if group_id:
        group_to_move_to = get_object_or_404(Group, id=group_id)
    if widget.group:
        for grouped_widget in widget.group.widgets():
            if grouped_widget.group_position > widget.group_position:
                grouped_widget.group_position -= 1
                grouped_widget.save()
    if group_to_move_to:
        widget.group_position = group_to_move_to.largest_widget_position() + 1
    else:
        widget.group_position = 0
    widget.group = group_to_move_to
    widget.save()

def widget_reposition(widget_id, position):
    widget = get_object_or_404(Widget, id=widget_id)
    position_to_move_to = int(position)
    if widget.group:
        largest_position = widget.group.largest_widget_position()
        if largest_position < position_to_move_to:
            position_to_move_to = largest_position
        if position_to_move_to > widget.group_position:
            for grouped_widget in widget.group.widgets():
                if grouped_widget.group_position > widget.group_position:
                    if grouped_widget.group_position <= position_to_move_to:
                        grouped_widget.group_position -= 1
                        grouped_widget.save()
        if position_to_move_to < widget.group_position:
            for grouped_widget in widget.group.widgets():
                if grouped_widget.group_position < widget.group_position:
                    if grouped_widget.group_position >= position_to_move_to:
                        grouped_widget.group_position += 1
                        grouped_widget.save()
        widget.group_position = position_to_move_to
        widget.save()