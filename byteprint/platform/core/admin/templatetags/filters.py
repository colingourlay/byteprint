from django import template

register = template.Library()

@register.filter
def object_type(obj, type_string):
    """
    Checks the type of an object against a string

    Usage:

    {% if form|obj_type:'mycustomform' %}
      <form class="custom" action="">
    {% else %}
      <form action="">
    {% endif %}

    """
    
    try:
        t = obj.__class__.__name__
        return t.lower() == str(type_string).lower()
    except:
        pass
    return False

@register.filter
def field_type(field, type_string):
    """
    Checks the type of a form field against a string

    Usage:

    {% if field|field_type:'checkboxinput' %}
      <label class="cb_label">{{ field }} {{ field.label }}</label>
    {% else %}
      <label for="id_{{ field.name }}">{{ field.label }}</label> {{ field }}
    {% endif %}

    """
    
    return object_type(field.field.widget, type_string)
