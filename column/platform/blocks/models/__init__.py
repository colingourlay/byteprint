from django.db import models
from platform.blocks import AbstractPlugin

class Block(models.Model):
    plugin_name = models.CharField(max_length=30)
    data = models.TextField()
    is_published = models.BooleanField()

    class Meta:
        app_label = 'blocks'
        verbose_name = 'block'
        verbose_name_plural = 'blocks'

    def __unicode__(self):
        return self.plugin_name

    def create(plugin_name, data_dict):
        """
        Returns True if Block was created, False if there was a problem,
        or if no matching plugin exists.
        """
        for plugin in AbstractPlugin.plugins:
            if plugin.__name__ == plugin_name:
                try:
                    plugin().create(plugin_name, data_dict)
                    return True
                except:
                    return False
        return False