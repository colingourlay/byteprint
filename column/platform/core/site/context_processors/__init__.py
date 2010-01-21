from django.conf import settings
from platform.core.settings.models import Setting

def request(request):
    extra_context = {}
    try:
        templatable_settings = Setting.objects.templatable()
        for setting in templatable_settings:
            extra_context[setting.key] = setting.value
        extra_context['content'] = settings.MEDIA_URL + 'themes/' + extra_context['theme']  + '/'
    except:
        pass  
    return extra_context