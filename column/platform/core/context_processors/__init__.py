from django.conf import settings
from platform.core.models import Definition
from platform.widgets.models import Widget
from platform.widgets.utils import render_widget

def request(request):
    extra_context = {}
    
    # TEMPLATABLE DEFNITIONS
    try:
        templatable_definitions = Definition.objects.filter_templatable()
        for definition in templatable_definitions:
            extra_context[definition.name] = definition.value
        extra_context['content'] = settings.MEDIA_URL + 'themes/' + extra_context['theme']  + '/'
    except:
        pass
    
    # PAGE WIDGETS    
    try:
        # TODO Change this to use a custom global filter once widgets have a manager. 
        # TODO It should return the pre-rendered content, so that a minumum amount of work is to be done in the template
        page_widgets = ""
        widgets = Widget.objects.all()
        for widget in widgets:
            page_widgets += render_widget(widget)
        extra_context['page_widgets'] = page_widgets
    except:
        pass
    
    # RETURN EXTRA CONTEXT    
    return extra_context