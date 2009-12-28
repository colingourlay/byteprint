from django.conf import settings
from platform.core.models import Definition

def request(request):
    extra_context = {}
    try:
        templatable_definitions = Definition.objects.filter_templatable()
        for definition in templatable_definitions:
            extra_context[definition.name] = definition.value
        extra_context['content'] = settings.MEDIA_URL + 'themes/' + extra_context['theme']  + '/'
    except:
        pass
    return extra_context