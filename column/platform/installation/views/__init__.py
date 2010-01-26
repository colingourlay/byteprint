from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from platform.core.settings.models import Setting
from platform.installation import is_installed
from platform.installation.forms import InstallationForm

def init_platform(request):
    
    if is_installed():
        return HttpResponseRedirect(reverse('admin'))
    
    if request.method == 'POST':
        installation_form = InstallationForm(request.POST)
        if installation_form.is_valid():
            
            # Initialise the admin account
            username = installation_form.cleaned_data['username']
            password = installation_form.cleaned_data['password']
            email = installation_form.cleaned_data['email']
            all_users = User.objects.all()
            all_users.delete()
            admin_user = User.objects.create_superuser(username, email, password)
            # Initialise the starting definitions
            
            all_settings = Setting.objects.all()
            all_settings.delete()
            theme_setting = Setting.objects.add_templatable('theme', 'default')
            blog_title = installation_form.cleaned_data['blog_title']
            blog_title_setting = Setting.objects.add_templatable('blog_title', blog_title)
            blog_subtitle_setting = Setting.objects.add_templatable('blog_subtitle', 'Just another Column weblog')
            widget_div_class_setting = Setting.objects.add_templatable('widget_div_class', 'widget')
            
            # Redirect the user to the admin interface
            return HttpResponseRedirect(reverse('admin'))  
    else:
        installation_form = InstallationForm()

    return render_to_response('installation/init_platform.html', RequestContext(request, {
        'form': installation_form, 'version': settings.VERSION,
    }))