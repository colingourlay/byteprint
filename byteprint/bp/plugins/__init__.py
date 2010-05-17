import os

__all__ = os.walk(os.path.dirname(__file__)).next()[1]

for plugin in __all__:
    exec "from bp.plugins import %s" % plugin