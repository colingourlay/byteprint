from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from platform.admin.forms.settings import GeneralSettingsForm
from platform.core.models import Definition

@login_required
def general(request):
    msg = None
    
    blog_title_definition = Definition.objects.get(name='blog_title')
    blog_subtitle_definition = Definition.objects.get(name='blog_subtitle')
    admin_user = User.objects.get(id=request.user.id)
    
    data = {'blog_title': blog_title_definition.value,
            'blog_subtitle': blog_subtitle_definition.value,
            'admin_email': admin_user.email}
            
    general_settings_form = GeneralSettingsForm(data)
                                
    if request.method == 'POST':
        general_settings_form = GeneralSettingsForm(request.POST)
        if general_settings_form.is_valid():

            # Update Definitions
            
            blog_title_definition.value = general_settings_form.cleaned_data['blog_title']
            blog_title_definition.save()
            blog_subtitle_definition.value = general_settings_form.cleaned_data['blog_subtitle']
            blog_subtitle_definition.save()
            
            # Update User
            admin_user.email = general_settings_form.cleaned_data['admin_email']
            admin_user.save()
            
            # Set success notification
            msg = "Your settings were updated"
            
    return render_to_response('admin/settings.html', RequestContext(request, {
        'form': general_settings_form, 'notification': msg,
    }))