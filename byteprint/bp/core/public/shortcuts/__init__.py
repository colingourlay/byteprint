from django.views.generic.simple import direct_to_template
from django.template import RequestContext

def direct_to_theme(request, template, extra_context={}):
    template = RequestContext(request)['theme'] + '/' + template
    return direct_to_template(
        request,
        template,
        extra_context
    )