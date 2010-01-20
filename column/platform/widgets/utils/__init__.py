import pickle
from django import forms
from django.shortcuts import get_object_or_404
from platform.widgets import Blueprint
from platform.widgets.models import Group, Widget

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

def build_widget(blueprint_name):
    try:
        blueprint = get_blueprint(blueprint_name)
        try:
            widget_data = {}
            for key, value in blueprint.fields.items():
                widget_data[key] = value.initial or ""
            pickled_widget_data = pickle.dumps(widget_data)
            widget = Widget(blueprint_name=blueprint_name, data=pickled_widget_data)
            widget.save()
            return widget
        except:
            return None
    except:
        return None

def get_edit_widget_form(widget):
    blueprint = get_blueprint(widget.blueprint_name)
    return type('EditWidgetForm', (forms.BaseForm,), { 'base_fields': blueprint.fields})

def get_edit_widget_form_instance(widget):
    edit_widget_form_class = get_edit_widget_form(widget)
    widget_data = pickle.loads(str(widget.data))
    return edit_widget_form_class(widget_data)

def widget_has_preview(widget):
    blueprint = get_blueprint(widget.blueprint_name)
    try:
        return blueprint.preview
    except:
        return False

def render_widget(widget):
    blueprint = get_blueprint(widget.blueprint_name)
    if blueprint:
        return blueprint().render(pickle.loads(str(widget.data)))
    return ""

def regroup_widget(widget_id, group_id):
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

def reposition_widget(widget_id, position):
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