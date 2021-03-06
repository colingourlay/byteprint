from operator import attrgetter
import re

from django import forms
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import Context
from django.template.loader import get_template
from django.utils.datastructures import SortedDict

from bp.core.scraps import Blueprint
from bp.core.scraps.models import Pile, Scrap
from bp.core.public import utils as public_utils

def get_blueprints(two_tuple=False, families=False):
    blueprints = []
    for blueprint in sorted(Blueprint.inventory, key=attrgetter('family')):
        if two_tuple:
            if families:
                blueprints.append((blueprint.name, blueprint.family + " | " + blueprint.display_name))
            else:
                blueprints.append((blueprint.name, blueprint.display_name))
        else:
            blueprints.append(blueprint.name)
    return blueprints

def get_blueprint(blueprint_name):
    for blueprint in Blueprint.inventory:
        if blueprint.name == blueprint_name:
            return blueprint
    return None

def pile_get(pile_id):
    return get_object_or_404(Pile, id=pile_id)

def pile_delete(pile_id):
    pile = pile_get(pile_id)
    scraps = pile.scraps()
    for scrap in scraps:
        scrap.pile = None
        scrap.pile_position = 0
        scrap.save()
    pile.delete()
    
def pile_toggle(pile_id, status):
    pile = get_object_or_404(Pile, id=pile_id, is_standalone=True)
    pile.is_enabled = status
    pile.save()
        
def scrap_create(blueprint_name):
    try:
        blueprint = get_blueprint(blueprint_name)
        try:
            scrap_data = {}
            for key, value in blueprint.fields.items():
                scrap_data[key] = value.initial or ""
            scrap = Scrap(blueprint_name=blueprint_name, data="")
            scrap.data_dump(scrap_data)
            scrap.title = blueprint.display_name or blueprint.name
            scrap.save()
            return scrap
        except:
            return None
    except:
        return None
        
def scrap_get(scrap_id):
    return get_object_or_404(Scrap, id=scrap_id)

def scrap_update(scrap, post_dict):
    blueprint = get_blueprint(scrap.blueprint_name)
    scrap_data = {}
    for key, value in blueprint.fields.items():
        scrap_data[key] = post_dict[key]
    scrap.data_dump(scrap_data)
    if 'scrap_title_text' in post_dict.keys():
        scrap.title = post_dict['scrap_title_text']
    scrap.save()

def scrap_get_edit_form(scrap, include_scrap_title=True):
    blueprint = get_blueprint(scrap.blueprint_name)
    fields = SortedDict()
    if include_scrap_title:
        fields['scrap_title_text'] = forms.CharField(
            label = "Scrap Title",
            help_text = "The title you enter here will appear above the scrap. \
                If you do not want a title to appear, leave this field blank.",
            initial = scrap.title,
            required = False,
        )
    for key, value in blueprint.fields.items():
        fields[key] = value
    return type('EditScrapForm', (forms.BaseForm,), { 'base_fields': fields})

def scrap_edit_form_instance(scrap, include_scrap_title=True):
    ScrapEditForm = scrap_get_edit_form(scrap, include_scrap_title)
    if include_scrap_title:
        scrap_fields = dict({'scrap_title_text': scrap.title}.items() + scrap.data_load().items())
    else:
        scrap_fields = dict(scrap.data_load().items())
    return ScrapEditForm(scrap_fields)

def scrap_delete(scrap_id):
    scrap = get_object_or_404(Scrap, id=scrap_id)
    scrap_repile(scrap_id, None)
    scrap.delete()

def scrap_has_preview(scrap):
    return get_blueprint(scrap.blueprint_name).preview

def scrap_render(scrap, show_title=True):
    blueprint = get_blueprint(scrap.blueprint_name)
    if blueprint:
        try:
            rendered_scrap = ""
            if scrap.title and show_title:
                rendered_scrap += "<h3>" + scrap.title + "</h3>"
            rendered_scrap += blueprint().render(scrap.data_load())
            return rendered_scrap, True
        except:
            return "<!-- " + blueprint.display_name + " failed to render -->", False
    return "<!-- " + scrap.blueprint_name + " is not a blueprint -->", False

def scrap_toggle(scrap_id, status):
    scrap = get_object_or_404(Scrap, id=scrap_id)
    scrap.is_enabled = status
    scrap.save()

def scrap_repile(scrap_id, pile_id):
    scrap = get_object_or_404(Scrap, id=scrap_id)
    pile_to_move_to = None
    if pile_id:
        pile_to_move_to = get_object_or_404(Pile, id=pile_id)
    if scrap.pile:
        for pileed_scrap in scrap.pile.scraps():
            if pileed_scrap.pile_position > scrap.pile_position:
                pileed_scrap.pile_position -= 1
                pileed_scrap.save()
    if pile_to_move_to:
        scrap.pile_position = pile_to_move_to.largest_scrap_position() + 1
    else:
        scrap.pile_position = 0
    scrap.pile = pile_to_move_to
    scrap.save()

def scrap_reposition(scrap_id, position):
    scrap = get_object_or_404(Scrap, id=scrap_id)
    position_to_move_to = int(position)
    if scrap.pile:
        largest_position = scrap.pile.largest_scrap_position()
        if largest_position < position_to_move_to:
            position_to_move_to = largest_position
        if position_to_move_to > scrap.pile_position:
            for pileed_scrap in scrap.pile.scraps():
                if pileed_scrap.pile_position > scrap.pile_position:
                    if pileed_scrap.pile_position <= position_to_move_to:
                        pileed_scrap.pile_position -= 1
                        pileed_scrap.save()
        if position_to_move_to < scrap.pile_position:
            for pileed_scrap in scrap.pile.scraps():
                if pileed_scrap.pile_position < scrap.pile_position:
                    if pileed_scrap.pile_position >= position_to_move_to:
                        pileed_scrap.pile_position += 1
                        pileed_scrap.save()
        scrap.pile_position = position_to_move_to
        scrap.save()

def asyncPileBodyRefresh(scrap_id):
    scrap = scrap_get(scrap_id)
    piles = Pile.objects.standalone()
    response = '<ul class="pane_list scrap_list">'
    if scrap.pile:
        pile_scraps = scrap.pile.scraps()
    else:
        pile_scraps = Scrap.objects.unpiled()
    pile_scraps_len = len(pile_scraps)
    for i, item in enumerate(pile_scraps):
        forloop = {}
        forloop['first'] = (i == 0)
        forloop['last'] = (i == pile_scraps_len - 1)
        response += get_template(
            'scraps/admin/includes/pile_list_item.html'
        ).render(Context({
            'scrap': item, 
            'piles': piles,
            'forloop': forloop
        }))
    response += '</ul>'
    return HttpResponse(response)

def asyncPileHeaderRefresh(pile_id):
    pile = pile_get(pile_id)
    response = get_template(
        'scraps/admin/includes/pile_header.html'
    ).render(Context({
        'pile': pile
    }))
    return HttpResponse(response)

def asyncAllPilesRefresh():
    piles = Pile.objects.standalone()
    unpiled_scraps = Scrap.objects.unpiled()
    response = get_template(
        'scraps/admin/includes/all_piles.html'
    ).render(Context({
        'piles': piles,
        'unpiled_scraps': unpiled_scraps
    }))
    return HttpResponse(response)