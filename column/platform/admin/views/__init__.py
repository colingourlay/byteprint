from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required
def portal(request):
    return render_to_response('admin/portal.html', RequestContext(request))