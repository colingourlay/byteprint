from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from platform.widgets.forms import BuildWidgetForm
from platform.widgets.models import Widget
from platform.widgets.utils import build_widget

@login_required
def manage(request):
    widgets = Widget.objects.all()
    build_widget_form = BuildWidgetForm()
    return render_to_response('admin/widgets/manage.html', {
        'menu_current': 'widgets_manage', 'h1': 'Manage Widgets',
        'widgets': widgets, 'form': build_widget_form}, RequestContext(request))

@login_required
def build(request):
    if request.method == 'POST':
        build_widget_form = BuildWidgetForm(request.POST)
        if build_widget_form.is_valid():
            blueprint_name = build_widget_form.cleaned_data['blueprint_name']
            widget, status = build_widget(blueprint_name)
            #we're not using the status yet
            if widget != None:
                return HttpResponseRedirect(reverse('admin_widgets_edit', kwargs={'widget_id': widget.id}))
    return HttpResponseRedirect(reverse('admin_widgets_manage'))

@login_required
def edit(request, widget_id):
    #need to implement get_object_or_404
    widget = Widget.objects.get(id=widget_id)
    return render_to_response('admin/widgets/edit.html', {
        'menu_current': 'widgets_manage', 'h1': 'Editing Widget',
        'widget': widget}, RequestContext(request))

@login_required
def delete(request, widget_id):
    #need to implement get_object_or_404
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    return HttpResponseRedirect(reverse('admin_widgets_manage'))