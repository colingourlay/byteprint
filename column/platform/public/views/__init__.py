from django.template import RequestContext
from platform.public.shortcuts import render_using_theme

def homepage(request):
    return render_using_theme('page.html', RequestContext(request))
