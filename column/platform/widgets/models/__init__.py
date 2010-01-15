from django.db import models

class WidgetManager(models.Manager):
    def ungrouped(self):
        widgets = self.all()
        ungrouped_widgets = []
        for widget in widgets:
            if not widget.is_grouped():
                ungrouped_widgets.append(widget)
        return ungrouped_widgets
    
    def in_group(self, group):
        widgets = self.all()
        widgets_in_group = []
        for widget in widgets:
            if widget.group() == group:
                widgets_in_group.append(widget)
        return widgets_in_group

class Widget(models.Model):
    blueprint_name = models.CharField(max_length=30)
    data = models.TextField()
    is_enabled = models.BooleanField(default=True)
    
    class Meta:
        app_label = 'widgets'
        verbose_name = 'widget'
        verbose_name_plural = 'widgets'
    
    objects = WidgetManager()
    
    def __unicode__(self):
        return self.blueprint_name
    
    def group(self):
        matching_containers = Container.objects.filter(widgets__id=self.id)
        if matching_containers.count() > 0:
            return matching_containers[0]
        return False
    
    def is_grouped(self):
        if self.group():
            return True
        return False

class Container(models.Model):
    name = models.CharField(max_length=30)
    widgets = models.ManyToManyField(Widget)
    
    def __unicode__(self):
        return self.name
    
    def get_widgets(self):
        return Widget.objects.in_group(self)
    

