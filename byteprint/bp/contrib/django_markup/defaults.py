# The list of automatically loaded MarkupFilters
from bp.contrib.django_markup.filter.linebreaks_filter import LinebreaksMarkupFilter
from bp.contrib.django_markup.filter.markdown_filter import MarkdownMarkupFilter
from bp.contrib.django_markup.filter.textile_filter import TextileMarkupFilter
from bp.contrib.django_markup.filter.rst_filter import RstMarkupFilter
from bp.contrib.django_markup.filter.smartypants_filter import SmartyPantsMarkupFilter
from bp.contrib.django_markup.filter.none_filter import NoneMarkupFilter
from bp.contrib.django_markup.filter.creole_filter import CreoleMarkupFilter
from bp.contrib.django_markup.filter.lightbox_filter import LightboxMarkupFilter
from bp.contrib.django_markup.filter.widont_filter import WidontMarkupFilter

# MarkupFilter that get's loaded automatically
# You can override this list within your settings: MARKUP_FILTER

DEFAULT_MARKUP_FILTER = {
    'creole': CreoleMarkupFilter,
    'linebreaks': LinebreaksMarkupFilter,
    'lightbox': LightboxMarkupFilter,
    'markdown': MarkdownMarkupFilter,
    'none': NoneMarkupFilter,
    'restructuredtext': RstMarkupFilter,
    'smartypants': SmartyPantsMarkupFilter,
    'textile': TextileMarkupFilter,
    'widont': WidontMarkupFilter,
}

# MarkupFilter that are the default value for choices, used in the MarkupField
# You can override this list within your settings: MARKUP_CHOICES

DEFAULT_MARKUP_CHOICES = (
    'linebreaks',
    'markdown',
    'restructuredtext',
    'textile',
    'creole',
)