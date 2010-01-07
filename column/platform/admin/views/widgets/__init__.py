from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from platform.widgets.utils import build_widget

@login_required
def build(request, blueprint_name):
    widget, status = build_widget(blueprint_name)
    return HttpResponse(status)

@login_required
def edit(request, widget_id):
    return HttpResponse("editing widget: " + widget_id)

@login_required
def list(request):
    return HttpResponse("list of widgets")
