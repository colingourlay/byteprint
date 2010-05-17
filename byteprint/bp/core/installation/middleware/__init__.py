from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from bp.core.installation import is_installed

class InstallationMiddleware(object):

    def process_request(self, request):
        if request.path.startswith('/static/') or request.path == "/favicon.ico":
            return None
        if request.path == reverse('installation_install'):
            return None
        if is_installed():
            return None
        return redirect('installation_install')