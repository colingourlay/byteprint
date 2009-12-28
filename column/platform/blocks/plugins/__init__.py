from platform.blocks import AbstractPlugin
from platform.blocks.models import Block

class TextBlockPlugin(AbstractPlugin):
    
    __name__ = 'TextBlockPlugin'
    
    def create(self, data_dict):
        print 'Created Text Block'
        
class ImageReferenceBlockPlugin(AbstractPlugin):
    
    __name__ = 'ImageReferenceBlockPlugin'
    
    def create(self, data_dict):
        print 'Created Image Reference Block'