from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from platform.widgets import Blueprint

@login_required
def list(request):
    blueprints = []
    for blueprint in Blueprint.inventory:
        blueprints.append(blueprint.name)
    return render_to_response('admin/blueprints/list.html',
        {'blueprints': blueprints, 'menu_current': 'blueprints_list'},
        RequestContext(request))