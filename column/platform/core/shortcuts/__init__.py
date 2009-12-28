import os
from django.shortcuts import render_to_response

def render_using_theme(template_name, request_context):
    return render_to_response(request_context['theme'] + '/' + template_name, request_context)