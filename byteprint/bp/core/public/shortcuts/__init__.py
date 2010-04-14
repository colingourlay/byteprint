import os

from django.shortcuts import render_to_response

def render_using_theme(template_name, context_instance, dictionary=None):
    dictionary = dictionary or {}
    return render_to_response(context_instance['theme'] + '/' + template_name, dictionary, context_instance)