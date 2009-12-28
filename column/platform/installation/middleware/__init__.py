from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
from django.core.management.commands import syncdb
from platform.installation.views import init_database, init_platform

class InstallationMiddleware(object):

    def process_request(self, request):
        if settings.DATABASE_ENGINE != 'dummy':
            try:
                try:
                    syncdb_command = syncdb.Command()
                    syncdb_command.handle_noargs()
                except Exception, e:
                    return init_database(request, e)
                else:
                    # TODO: fix for admin user only
                    if len(User.objects.filter(is_superuser=True)) > 0:
                        return
            except:
                return init_database(request)
            else:
                return init_platform(request)
        return init_platform(request)