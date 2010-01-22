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
from platform.core.widgets import utils
from platform.core.widgets.forms import CreateWidgetForm, CreateGroupForm
from platform.core.widgets.models import Group, Widget
from platform.core.widgets.utils import get_blueprint

@login_required
def manage(request):
    groups = Group.objects.standalone()
    widgets = Widget.objects.all()
    ungrouped_widgets = Widget.objects.ungrouped()
    create_widget_form = CreateWidgetForm()
    create_group_form = CreateGroupForm()
    return render_to_response(
        'admin/widgets/manage.html', {
            'menu_current': 'widgets_manage', 'h1': 'Manage Widgets',
            'groups': groups, 'widgets': widgets,
            'ungrouped_widgets': ungrouped_widgets,
            'create_widget_form': create_widget_form,
            'create_group_form': create_group_form},
        RequestContext(request))

@login_required
def group_create(request):
    if request.method == 'POST':
        create_group_form = CreateGroupForm(request.POST)
        if create_group_form.is_valid():
            name = create_group_form.cleaned_data['name']
            group = Group(name=name,is_standalone=True)
            group.save()
    return HttpResponseRedirect(reverse('admin_widgets_manage'))

@login_required
def group_delete(request, group_id):
    utils.group_delete(group_id)
    return HttpResponseRedirect(reverse('admin_widgets_manage'))

@login_required
def widget_create(request):
    if request.method == 'POST':
        create_widget_form = CreateWidgetForm(request.POST)
        if create_widget_form.is_valid():
            blueprint_name = create_widget_form.cleaned_data['blueprint_name']
            widget = utils.widget_create(blueprint_name)
            #return HttpResponseRedirect(reverse('admin_widgets_edit', kwargs={'widget_id':widget.id}))
    return HttpResponseRedirect(reverse('admin_widgets_manage'))

@login_required
def widget_edit(request, widget_id):
    widget = utils.widget_get(widget_id)
    msg = None
    if request.method == 'POST':
        widget_edit_form = utils.widget_get_edit_form(widget)
        widget_edit_form = widget_edit_form(request.POST)
        if widget_edit_form.is_valid():
            utils.widget_update(widget, request.POST)
            msg = 'Your changes to this ' + widget.blueprint_display_name() + ' widget were saved'
    else:
        widget_edit_form = utils.widget_edit_form_instance(widget)
    h1 = "Editing " + widget.blueprint_display_name() + " Widget"
    show_preview = utils.widget_has_preview(widget)
    return render_to_response('admin/widgets/edit.html', {
        'menu_current': 'widgets_manage', 'h1': h1,
        'widget': widget, 'show_preview': show_preview,
        'form': widget_edit_form, 'msg': msg}, RequestContext(request))

@login_required
def widget_delete(request, widget_id):
    utils.widget_delete(widget_id)
    return HttpResponseRedirect(reverse('admin_widgets_manage'))

@login_required
def widget_toggle(request, widget_id, status):
    utils.widget_toggle(widget_id, status)
    return HttpResponseRedirect(reverse('admin_widgets_manage'))

@login_required
def widget_regroup(request, widget_id, group_id=None):
    utils.widget_regroup(widget_id, group_id)
    return HttpResponseRedirect(reverse('admin_widgets_manage'))
    
@login_required
def widget_reposition(request, widget_id, position):
    utils.widget_reposition(widget_id, position)
    return HttpResponseRedirect(reverse('admin_widgets_manage'))