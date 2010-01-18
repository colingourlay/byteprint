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
from platform.widgets.forms import BuildWidgetForm, CreateGroupForm
from platform.widgets.models import Group, Widget
from platform.widgets.utils import build_widget, get_blueprint, get_edit_widget_form, get_edit_widget_form_instance, reposition_widget, regroup_widget, widget_has_preview

@login_required
def manage(request):
    groups = Group.objects.all()
    widgets = Widget.objects.all()
    ungrouped_widgets= Widget.objects.ungrouped()
    build_widget_form = BuildWidgetForm()
    create_group_form = CreateGroupForm()
    return render_to_response(
        'admin/widgets/manage.html', {
            'menu_current': 'widgets_manage', 'h1': 'Manage Widgets',
            'groups': groups, 'widgets': widgets,
            'ungrouped_widgets': ungrouped_widgets,
            'build_widget_form': build_widget_form,
            'create_group_form': create_group_form},
        RequestContext(request))

@login_required
def build(request):
    if request.method == 'POST':
        build_widget_form = BuildWidgetForm(request.POST)
        if build_widget_form.is_valid():
            blueprint_name = build_widget_form.cleaned_data['blueprint_name']
            widget = build_widget(blueprint_name)
    return HttpResponseRedirect(reverse('admin_widgets_manage'))
    #return HttpResponseRedirect(reverse('admin_widgets_edit', kwargs={'widget_id':widget.id}))

@login_required
def edit(request, widget_id):
    widget = get_object_or_404(Widget, id=widget_id)
    show_preview = widget_has_preview(widget)
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
        'widget': widget, 'show_preview': show_preview,
        'form': edit_widget_form, 'msg': msg}, RequestContext(request))

@login_required
def delete(request, widget_id):
    widget = get_object_or_404(Widget, id=widget_id)
    widget.delete()
    return HttpResponseRedirect(reverse('admin_widgets_manage'))
    
@login_required
def add_group(request):
    if request.method == 'POST':
        create_group_form = CreateGroupForm(request.POST)
        if create_group_form.is_valid():
            name = create_group_form.cleaned_data['name']
            group = Group(name=name)
            group.save()
    return HttpResponseRedirect(reverse('admin_widgets_manage'))

@login_required
def delete_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    widgets = group.widgets()
    for widget in widgets:
        widget.group = None
        widget.group_position = 0
        widget.save()
    group.delete()
    return HttpResponseRedirect(reverse('admin_widgets_manage'))

@login_required
def toggle(request, widget_id, status):
    widget = get_object_or_404(Widget, id=widget_id)
    widget.is_enabled = status
    widget.save()
    return HttpResponseRedirect(reverse('admin_widgets_manage'))

@login_required
def regroup(request, widget_id, group_id=None):
    regroup_widget(widget_id, group_id)
    return HttpResponseRedirect(reverse('admin_widgets_manage'))
    
@login_required
def reposition(request, widget_id, position):
    reposition_widget(widget_id, position)
    return HttpResponseRedirect(reverse('admin_widgets_manage'))