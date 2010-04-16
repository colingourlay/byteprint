from django.conf import settings

from bp.core.config.models import Setting

def get_public_context():
    public_context = {}
    try:
        templatable_settings = Setting.objects.templatable()
        for setting in templatable_settings:
            public_context[setting.key] = setting.value
        public_context['static'] = settings.MEDIA_URL + 'themes/' + public_context['theme']  + '/'
    except:
        pass  
    return public_context