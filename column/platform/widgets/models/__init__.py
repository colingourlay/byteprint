from django.db import models

class Widget(models.Model):
    blueprint_name = models.CharField(max_length=30)
    data = models.TextField()
    is_enabled = models.BooleanField(default=True)
    
    class Meta:
        app_label = 'widgets'
        verbose_name = 'widget'
        verbose_name_plural = 'widgets'
    
    def __unicode__(self):
        return self.blueprint_name
    
    def container(self):
        matching_containers = Container.objects.filter(widgets__id=self.id)
        if matching_containers.count() > 0:
            return matching_containers[0]
        return False
    
    def is_in_any_container(self):
        if self.container():
            return True
        return False
    

class Container(models.Model):
    name = models.CharField(max_length=30)
    widgets = models.ManyToManyField(Widget)
    
    def __unicode__(self):
        return self.name
    

