from django.db import models

class DefinitionManager(models.Manager):
    def add(self, name, value, is_templatable=False):
        definition = self.model(None, name, value, is_templatable)
        definition.save()
        return definition
    
    def add_templatable(self, name, value):
        definition = self.model(None, name, value, True)
        definition.save()
        return definition
    
    def get_value(self, name):
        try:
            return self.get(name=name).value
        except:
            return None
    
    def filter_templatable(self):
        return self.filter(is_templatable=True)

class Definition(models.Model):
    name = models.CharField(max_length=40)
    value = models.TextField()
    is_templatable = models.BooleanField()
    
    objects = DefinitionManager()

    class Meta:
        app_label = 'core'
        verbose_name = 'definition'
        verbose_name_plural = 'definitions'

    def __unicode__(self):
        return self.name