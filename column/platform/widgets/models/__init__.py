from django.db import models

class WidgetManager(models.Manager):
    def ungrouped(self):
        return self.filter(group__isnull=True)
    
    def in_group(self, group):
        return self.filter(group=group)

class Widget(models.Model):
    blueprint_name = models.CharField(max_length=30)
    data = models.TextField()
    is_enabled = models.BooleanField(default=False)
    group = models.ForeignKey('Group', null=True)
    group_position = models.PositiveIntegerField(default=0)
    
    class Meta:
        app_label = 'widgets'
        verbose_name = 'widget'
        verbose_name_plural = 'widgets'
        ordering = ('group_position',)
        #unique_together = ("group", "group_position")
    
    objects = WidgetManager()
    
    def __unicode__(self):
        return self.blueprint_name

class Group(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __unicode__(self):
        return self.name
    
    def widgets(self):
        return Widget.objects.in_group(self)
    
    def largest_widget_position(self):
        return self.widgets.aggregate(Max('position')) or 0

    def smallest_widget_position(self):
        return self.widgets.aggregate(Min('position')) or 0
