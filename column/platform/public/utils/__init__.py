from django.conf import settings
from platform.config.models import Setting

def get_site_context():
    site_context = {}
    try:
        templatable_settings = Setting.objects.templatable()
        for setting in templatable_settings:
            site_context[setting.key] = setting.value
        site_context['content'] = settings.MEDIA_URL + 'themes/' + site_context['theme']  + '/'
    except:
        pass  
    return site_context