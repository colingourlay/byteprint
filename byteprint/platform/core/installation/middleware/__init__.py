from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from platform.core.installation import is_installed
from platform.core.installation.views import init_platform

class InstallationMiddleware(object):

    def process_request(self, request):
        if request.path.startswith('/static/'):
            return None
        if request.path == reverse('installation_init_platform'):
            return None
        if is_installed():
            return None
        return HttpResponseRedirect(reverse('installation_init_platform'))