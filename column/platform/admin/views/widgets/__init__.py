import pickle
from django import forms
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.text import capfirst
from platform.widgets.forms import BuildWidgetForm
from platform.widgets.models import Container, Widget
from platform.widgets.utils import build_widget, get_blueprint, get_edit_widget_form, get_edit_widget_form_instance, move_widget

@login_required
def manage(request):
    containers = Container.objects.all()
    widgets = Widget.objects.all()
    build_widget_form = BuildWidgetForm()
    return render_to_response('admin/widgets/manage.html', {
        'menu_current': 'widgets_manage', 'h1': 'Manage Widgets',
        'containers': containers, 'widgets': widgets,
        'form': build_widget_form}, RequestContext(request))

@login_required
def build(request):
    if request.method == 'POST':
        build_widget_form = BuildWidgetForm(request.POST)
        if build_widget_form.is_valid():
            blueprint_name = build_widget_form.cleaned_data['blueprint_name']
            widget = build_widget(blueprint_name)
    return HttpResponseRedirect(reverse('admin_widgets_edit', kwargs={'widget_id':widget.id}))

@login_required
def edit(request, widget_id):
    widget = get_object_or_404(Widget, id=widget_id)
    h1 = "Editing " + capfirst(widget.blueprint_name) + " Widget"
    msg = None
    if request.method == 'POST':
        edit_widget_form = get_edit_widget_form(widget)
        edit_widget_form = edit_widget_form(request.POST)
        if edit_widget_form.is_valid():
            widget.data = pickle.dumps(request.POST)
            widget.save()
            msg = 'Your changes to this ' + widget.blueprint_name + ' widget were saved'
    else:
        edit_widget_form = get_edit_widget_form_instance(widget)
    return render_to_response('admin/widgets/edit.html', {
        'menu_current': 'widgets_manage', 'h1': h1,
        'widget': widget, 'form': edit_widget_form, 'msg': msg}, RequestContext(request))

@login_required
def delete(request, widget_id):
    widget = get_object_or_404(Widget, id=widget_id)
    widget.delete()
    return HttpResponseRedirect(reverse('admin_widgets_manage'))

@login_required
def toggle(request, widget_id, status):
    widget = get_object_or_404(Widget, id=widget_id)
    widget.is_enabled = status
    widget.save()
    return HttpResponseRedirect(reverse('admin_widgets_manage'))

@login_required
def move_to_container(request, widget_id, container_id=None):
    move_widget(widget_id, container_id)
    return HttpResponseRedirect(reverse('admin_widgets_manage'))