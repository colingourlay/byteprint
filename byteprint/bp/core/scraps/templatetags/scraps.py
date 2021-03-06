import re

from django import template
from django.utils.datastructures import SortedDict

from bp.core.config.models import Setting
from bp.core.scraps.models import Pile, Scrap
from bp.core.scraps.utils import scrap_render

register = template.Library()

@register.simple_tag
def pile(pile_name):
    output = ""
    try:
        scrap_div_class = Setting.objects.get_value('scrap_div_class')
        piles = Pile.objects.filter(name=pile_name,is_standalone=True)
        if piles:
            for pile in piles:
                if pile.is_enabled:
                    scraps = Scrap.objects.in_pile(pile).filter(is_enabled=True)
                    if scraps:
                        for scrap in scraps:
                            rendered_scrap, was_successful = scrap_render(scrap)
                            if was_successful:
                                output += "<div class=\"" + scrap.blueprint_name + " " + scrap_div_class + "\">" + rendered_scrap + "</div>"
                            else:
                                output += rendered_scrap
                    else:
                        output += "<!-- scrap pile '" + pile_name + "' is empty -->"
                else:
                    output += "<!-- scrap pile '" + pile_name + "' is not enabled -->"
        else:
            output = "<!-- scrap pile '" + pile_name + "' was not found -->"
        return output
    except:
        output = "<!-- scrap pile '" + pile_name + "' was not found -->"
    return output

@register.simple_tag
def piles_list():
    output = ""
    try:
        piles = Pile.objects.standalone()
        if piles:
            for pile in piles:
                output += "<p class=\"pile\">" + pile.name + "</p>"
        else:
            output = "<!-- no piles found -->"
    except:
        output = "<!-- error loading piles -->"
    return output

@register.simple_tag
def scrap(scrap_id, show_title=True):
    output = ""
    try:
        scrap = Scrap.objects.get(id=scrap_id)
        rendered_scrap, was_successful = scrap_render(scrap, show_title=show_title) 
        output += rendered_scrap
    except:
        output = "<!-- scrap not found -->"
    return output

@register.simple_tag
def scrap_without_title(scrap_id):
    return scrap(scrap_id, show_title=False)

@register.simple_tag
def scrap_debug(scrap_id, show_title=True):
    output = scrap(scrap_id, show_title=show_title)
    output = re.sub('<!--', "<p class='negative'>", output)
    output = re.sub('-->', "</p>", output)
    return output

@register.simple_tag
def scrap_debug_without_title(scrap_id):
    return scrap_debug(scrap_id, show_title=False)