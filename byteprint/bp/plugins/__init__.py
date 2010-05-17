import os

__all__ = os.walk(os.path.dirname(__file__)).next()[1]

from bp.plugins import *