import pickle
from django.db import models
from django.db.models import Max, Min
from platform.core.widgets import Blueprint

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
        verbose_name = 'widget'
        verbose_name_plural = 'widgets'
        ordering = ('group_position',)
    
    objects = WidgetManager()
    
    def __unicode__(self):
        return self.blueprint_name
    
    def data_load(self):
        return pickle.loads(str(self.data))
    
    def data_dump(self, data):
        self.data = pickle.dumps(data)
    
    def blueprint_display_name(self):
        for blueprint in Blueprint.inventory:
            if blueprint.name == self.blueprint_name:
                return blueprint.display_name
        return self.blueprint_name
    
    def prev_group_position(self):
        if self.group_position == 0:
            return 0
        return self.group_position - 1

    def next_group_position(self):
        return self.group_position + 1

class GroupManager(models.Manager):
    def standalone(self):
        return self.filter(is_standalone=True)


class Group(models.Model):
    name = models.CharField(max_length=30)
    is_standalone = models.BooleanField(blank=False, default=True)
    is_enabled = models.BooleanField(default=True)
    
    objects = GroupManager()
    
    def __unicode__(self):
        return self.name
    
    def widgets(self):
        return Widget.objects.in_group(self)
    
    def largest_widget_position(self):
        if not self.widgets():
            return -1
        return self.widgets().aggregate(Max('group_position'))['group_position__max']

    def smallest_widget_position(self):   
        if not self.widgets():
            return -1
        return self.widgets().aggregate(Min('group_position'))['group_position__min']
