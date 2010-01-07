from django.db import models

class Widget(models.Model):
    blueprint_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    data = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        app_label = 'widgets'
        verbose_name = 'widget'
        verbose_name_plural = 'widgets'

    def __unicode__(self):
        return self.blueprint_name