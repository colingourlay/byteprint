from django.core.management.commands import syncdb
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from platform.core.settings.models import Setting
from platform.installation import is_installed
from platform.installation.forms import InstallationForm

def installed(request):
    return render_to_response(
        'installation/installed.html',
        RequestContext(
            request,
            {
                'version': settings.VERSION,
            }
        )
    )

def init_platform(request):
    
    if is_installed():
        return installed(request)
    
    db_error = ""
    
    if request.method == 'POST':
        installation_form = InstallationForm(request.POST)
        if installation_form.is_valid():
            try:
                # Initialise the database
                syncdb_command = syncdb.Command()
                syncdb_command.handle_noargs()
            except Exception, e:    
                db_error = e
            else:    
                # Initialise the admin account
                username = installation_form.cleaned_data['username']
                password = installation_form.cleaned_data['password']
                email = installation_form.cleaned_data['email']
                all_users = User.objects.all()
                all_users.delete()
                admin_user = User.objects.create_superuser(username, email, password)
                # Initialise the basic set of site settings
                blog_title = installation_form.cleaned_data['blog_title']
                blog_title_setting = Setting.objects.add_templatable('blog_title', blog_title)
                blog_email_setting = Setting.objects.add('blog_email', email)
                # Redirect the user to the admin interface
                return installed(request)
    else:
        installation_form = InstallationForm()

    return render_to_response(
        'installation/init_platform.html',
        RequestContext(
            request,
            {
                'form': installation_form,
                'version': settings.VERSION,
                'db_error': db_error,
            }
        )
    )