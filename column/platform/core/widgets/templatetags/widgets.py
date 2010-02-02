from django import template
from platform.core.settings.models import Setting
from platform.core.widgets.models import Group, Widget
from platform.core.widgets.utils import widget_render

register = template.Library()

@register.simple_tag
def group_widgets(group_name):
    output = ""
    try:
        widget_div_class = Setting.objects.get_value('widget_div_class')
        groups = Group.objects.filter(name=group_name,is_standalone=True)
        if groups:
            for group in groups:
                if group.is_enabled:
                    widgets = Widget.objects.in_group(group).filter(is_enabled=True)
                    if widgets:
                        for widget in widgets:
                            rendered_widget, was_successful = widget_render(widget)
                            if was_successful:
                                output += "<div class=\"" + widget.blueprint_name + " " + widget_div_class + "\">" + rendered_widget + "</div>"
                            else:
                                output += rendered_widget
                    else:
                        output += "<!-- Widget Group '" + group_name + "' is empty -->"
                else:
                    output += "<!-- Widget Group '" + group_name + "' is not enabled -->"
        else:
            output = "<!-- Widget Group '" + group_name + "' was not found -->"
        return output
    except:
        output = "<!-- Widget Group '" + group_name + "' was not found -->"
    return output

@register.simple_tag
def groups():
    output = ""
    try:
        groups = Group.objects.standalone()
        if groups:
            for group in groups:
                output += "<p class=\"group\">" + group.name + "</p>"
        else:
            output = "<!-- No Groups found -->"
    except:
        output = "<!-- Error loading Groups -->"
    return output

@register.simple_tag
def widget(widget_id):
    output = ""
    try:
        widget = Widget.objects.get(id=widget_id)
        rendered_widget, was_successful = widget_render(widget) 
        output += rendered_widget
    except:
        output = "<!-- Widget not found -->"
    return output

register.simple_tag(group_widgets)
register.simple_tag(groups)
register.simple_tag(widget)