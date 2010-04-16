from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.text import capfirst
from django.views.generic.simple import direct_to_template

from bp.core.admin.shortcuts import json_response
from bp.core.scraps import utils
from bp.core.scraps.forms import CreateScrapForm, CreatePileForm, RenamePileForm
from bp.core.scraps.models import Pile, Scrap

BLUEPRINTS_TEMPLATE = 'scraps/admin/blueprints.html'
MANAGE_TEMPLATE = 'scraps/admin/manage.html'
SCRAP_EDIT_TEMPLATE = 'scraps/admin/edit.html'

@login_required
def blueprints(request, template=BLUEPRINTS_TEMPLATE):
    blueprint_names = utils.get_blueprints()
    blueprints = []
    for name in blueprint_names:
        blueprints.append(utils.get_blueprint(name))
        
    return direct_to_template(
        request,
        template,
        {
            'menu_current': 'design_blueprints',
            'h1': 'Scrap Blueprints',
            'blueprints': blueprints
        }
    )
        
@login_required
def manage(request, template=MANAGE_TEMPLATE):
    piles = Pile.objects.standalone()
    scraps = Scrap.objects.all()
    unpiled_scraps = Scrap.objects.unpiled()
    create_scrap_form = CreateScrapForm()
    create_pile_form = CreatePileForm()
    return direct_to_template(
        request,
        template,
        {
            'menu_current': 'design_scraps',
            'h1': 'Manage Scraps',
            'piles': piles,
            'scraps': scraps,
            'unpiled_scraps': unpiled_scraps,
            'create_scrap_form': create_scrap_form,
            'create_pile_form': create_pile_form
        }
    )

@login_required
def pile_create(request):
    if request.method == 'POST':
        create_pile_form = CreatePileForm(request.POST)
        if create_pile_form.is_valid():
            name = create_pile_form.cleaned_data['name']
            pile = Pile(name=name,is_standalone=True)
            pile.save()
            if request.is_ajax():
                return utils.asyncAllPilesRefresh()
    return redirect('scraps_admin_manage')

@login_required
def pile_delete(request, pile_id):
    utils.pile_delete(pile_id)
    if request.is_ajax():
        return utils.asyncAllPilesRefresh()
    return redirect('scraps_admin_manage')
    
def pile_toggle(request, pile_id, status):
    utils.pile_toggle(pile_id, status)
    if request.is_ajax():
        return utils.asyncPileHeaderRefresh(pile_id)
    return redirect('scraps_admin_manage')

@login_required
def pile_rename(request, pile_id):
    pile = utils.pile_get(pile_id)
    if request.method == 'POST':
        rename_pile_form = RenamePileForm(request.POST, prefix=pile.id)
        if rename_pile_form.is_valid():
            if pile.name != rename_pile_form.cleaned_data['name']:
                old_pile_name = pile.name
                pile.name = rename_pile_form.cleaned_data['name']
                pile.save()
                if request.is_ajax():
                    msg = 'The scrap pile <strong>' + old_pile_name \
                        + '</strong> has been renamed to <strong>' \
                        + pile.name + '</strong>. Please check your template \
                        tags to ensure they match.'
                    return json_response({
                        'name': pile.name,'msg': msg
                    })
    return redirect('scraps_admin_manage')

@login_required
def scrap_create(request, blueprint_name=None):
    if blueprint_name:
        scrap = utils.scrap_create(blueprint_name)
    else:
        if request.method == 'POST':
            create_scrap_form = CreateScrapForm(request.POST)
            if create_scrap_form.is_valid():
                blueprint_name = create_scrap_form.cleaned_data['blueprint_name']
                scrap = utils.scrap_create(blueprint_name)
                if request.is_ajax():
                    return utils.asyncPileBodyRefresh(scrap.id)
    return redirect('scraps_admin_manage')

@login_required
def scrap_edit(request, scrap_id, template=SCRAP_EDIT_TEMPLATE):
    scrap = utils.scrap_get(scrap_id)
    msg = None
    if request.method == 'POST':
        scrap_edit_form = utils.scrap_get_edit_form(scrap)
        scrap_edit_form = scrap_edit_form(request.POST)
        if scrap_edit_form.is_valid():
            utils.scrap_update(scrap, request.POST)
            msg = 'Your changes to this ' + scrap.blueprint_display_name() \
                + ' scrap were saved'
    else:
        scrap_edit_form = utils.scrap_edit_form_instance(scrap)
    h1 = "Editing " + scrap.blueprint_display_name() + " Scrap"
    show_preview = utils.scrap_has_preview(scrap)
    
    return direct_to_template(
        request,
        template,
        {
            'menu_current': 'design_scraps',
            'h1': h1,
            'scrap': scrap,
            'show_preview': show_preview,
            'form': scrap_edit_form,
            'msg': msg
        }
    )

@login_required
def scrap_delete(request, scrap_id):
    utils.scrap_delete(scrap_id)
    if request.is_ajax():
        return utils.asyncAllPilesRefresh()
    return redirect('scraps_admin_manage')

@login_required
def scrap_toggle(request, scrap_id, status):
    utils.scrap_toggle(scrap_id, status)
    if request.is_ajax():
        return utils.asyncPileBodyRefresh(scrap_id)
    return redirect('scraps_admin_manage')

@login_required
def scrap_repile(request, scrap_id, pile_id=None):
    utils.scrap_repile(scrap_id, pile_id)
    if request.is_ajax():
        return utils.asyncAllPilesRefresh()
    return redirect('scraps_admin_manage')
    
@login_required
def scrap_reposition(request, scrap_id, position):
    utils.scrap_reposition(scrap_id, position)
    if request.is_ajax():
        return utils.asyncPileBodyRefresh(scrap_id)
    return redirect('scraps_admin_manage')