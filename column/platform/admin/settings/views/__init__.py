from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from platform.core.settings.forms import GeneralSettingsForm, ScrapsSettingsForm
from platform.core.settings.models import Setting

@login_required
def general(request, template_name='admin/settings/edit.html'):
    msg = None
    
    blog_title_setting = Setting.objects.get(key='blog_title')
    blog_subtitle_setting = Setting.objects.get(key='blog_subtitle')
    blog_email_setting = Setting.objects.get(key='blog_email')
    
    data = {'blog_title': blog_title_setting.value,
            'blog_subtitle': blog_subtitle_setting.value,
            'blog_email': blog_email_setting.value}
            
    general_settings_form = GeneralSettingsForm(data)
                                
    if request.method == 'POST':
        general_settings_form = GeneralSettingsForm(request.POST)
        if general_settings_form.is_valid():

            # Update settings
            
            blog_title_setting.value = general_settings_form.cleaned_data['blog_title']
            blog_title_setting.save()
            blog_subtitle_setting.value = general_settings_form.cleaned_data['blog_subtitle']
            blog_subtitle_setting.save()
            blog_email_setting.value = general_settings_form.cleaned_data['blog_email']
            blog_email_setting.save()
            
            # Set success notification
            msg = "Your settings were updated"
            
    return render_to_response(template_name, RequestContext(request, {
        'h1': 'General Settings', 'form': general_settings_form,
        'msg': msg, 'menu_current': 'settings_general',
    }))

@login_required
def scraps(request, template_name='admin/settings/edit.html'):
    msg = None

    scrap_div_class_setting = Setting.objects.get(key='scrap_div_class')

    data = {'scrap_div_class': scrap_div_class_setting.value}

    scraps_settings_form = ScrapsSettingsForm(data)

    if request.method == 'POST':
        scraps_settings_form = ScrapsSettingsForm(request.POST)
        if scraps_settings_form.is_valid():

            # Update settings
            scrap_div_class_setting.value = scraps_settings_form.cleaned_data['scrap_div_class']
            scrap_div_class_setting.save()

            # Set success notification
            msg = "Your settings were updated"

    return render_to_response(template_name, RequestContext(request, {
        'h1': 'Scraps Settings', 'form': scraps_settings_form,
        'msg': msg, 'menu_current': 'settings_scraps',
    }))