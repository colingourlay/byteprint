from django.db.models import get_model
from django.template import Library, Node, TemplateSyntaxError, Variable, resolve_variable

from bp.core.classification.models import ClassificationMapping

register = Library()

class ClassificationMappingsNode(Node):
    def __init__(self, obj, context_var):
        self.obj = Variable(obj)
        self.context_var = context_var

    def render(self, context):
        context[self.context_var] = \
            ClassificationMapping.objects.get_for_object(
                self.obj.resolve(context)
            )
        return ''

def do_classification_mappings(parser, token):
    """
    Retrieves a list of ``ClassificationMapping`` objects and stores them in a context variable.

    Usage::

       {% classification_mappings for [object] as [varname] %}

    Example::

        {% classification_mappings for article as article_classifications %}
    """
    bits = token.contents.split()
    if len(bits) != 5:
            raise TemplateSyntaxError(
            ('%s template tag requires exactly four arguments') % bits[0]
        )
    if bits[1] != 'for':
        raise TemplateSyntaxError(
            ("first argument in %s template tag must be 'for'") % bits[0]
        )
    if bits[3] != 'as':
        raise TemplateSyntaxError(
            ("third argument in %s template tag must be 'as'") % bits[0]
        )
    return ClassificationMappingsNode(bits[2], bits[4])

register.tag('classification_mappings', do_classification_mappings)
