from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.simple import direct_to_template

from bp.core.config.forms import GeneralSettingsForm, ScrapsSettingsForm
from bp.core.config.models import Setting

SETTINGS_EDIT_TEMPLATE = 'config/admin/edit.html'

@login_required
def general(request, template=SETTINGS_EDIT_TEMPLATE):
    msg = None
    
    site_title_setting = Setting.objects.get(key='site_title')
    site_subtitle_setting = Setting.objects.get(key='site_subtitle')
    site_email_setting = Setting.objects.get(key='site_email')
    
    data = {
        'site_title': site_title_setting.value,
        'site_subtitle': site_subtitle_setting.value,
        'site_email': site_email_setting.value
    }
            
    general_settings_form = GeneralSettingsForm(data)
                                
    if request.method == 'POST':
        general_settings_form = GeneralSettingsForm(request.POST)
        if general_settings_form.is_valid():

            # Update settings
            
            site_title_setting.value = general_settings_form.cleaned_data['site_title']
            site_title_setting.save()
            site_subtitle_setting.value = general_settings_form.cleaned_data['site_subtitle']
            site_subtitle_setting.save()
            site_email_setting.value = general_settings_form.cleaned_data['site_email']
            site_email_setting.save()
            
            # Set success notification
            msg = "Your settings were updated"
            
    return direct_to_template(
        request,
        template,
        {
            'h1': 'General Settings',
            'form': general_settings_form,
            'msg': msg,
            'menu_current': 'settings_general',
        }
    )

@login_required
def scraps(request, template=SETTINGS_EDIT_TEMPLATE):
    msg = None

    scrap_div_class_setting = Setting.objects.get(key='scrap_div_class')

    data = {
        'scrap_div_class': scrap_div_class_setting.value
    }

    scraps_settings_form = ScrapsSettingsForm(data)

    if request.method == 'POST':
        scraps_settings_form = ScrapsSettingsForm(request.POST)
        if scraps_settings_form.is_valid():

            # Update settings
            scrap_div_class_setting.value = scraps_settings_form.cleaned_data['scrap_div_class']
            scrap_div_class_setting.save()

            # Set success notification
            msg = "Your settings were updated"

    return direct_to_template(
        request,
        template,
        {
            'h1': 'Scraps Settings',
            'form': scraps_settings_form,
            'msg': msg,
            'menu_current': 'settings_scraps',
        }
    )