from django import template
from platform.widgets.models import Group, Widget
from platform.widgets.utils import render_widget

register = template.Library()

@register.simple_tag
def group_widgets(group_name):
    output = ""
    try:
        group = Group.objects.get(name=group_name)
        widgets = Widget.objects.in_group(group).filter(is_enabled=True)
        if widgets:
            for widget in widgets:
                output += "<div class=\"widget\">" + render_widget(widget) + "</div>"
        else:
            output = "<!-- Widget Group '" + group_name + "' is empty -->"
    except:
        output = "<!-- Widget Group '" + group_name + "' was not found -->"
    return output

@register.simple_tag
def groups():
    output = ""
    try:
        groups = Group.objects.all()
        if groups:
            for group in groups:
                output += "<p class=\"group\">" + group.name + "</p>"
        else:
            output = "<!-- No Groups found -->"
    except:
        output = "<!-- Error loading Groups -->"
    return output

@register.simple_tag
def widget_preview(widget_id):
    output = ""
    try:
        widget = Widget.objects.get(id=widget_id)
        output += render_widget(widget)
    except:
        output = "<!-- Widget not found -->"
    return output

register.simple_tag(group_widgets)
register.simple_tag(groups)
register.simple_tag(widget_preview)