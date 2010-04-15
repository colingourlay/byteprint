import pickle

from django.db import models
from django.db.models import Max, Min

from bp.core.scraps import Blueprint

class ScrapManager(models.Manager):
    def unpiled(self):
        return self.filter(pile__isnull=True)
    
    def in_pile(self, pile):
        return self.filter(pile=pile)

class Scrap(models.Model):
    blueprint_name = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=30)
    data = models.TextField()
    is_enabled = models.BooleanField(default=False)
    pile = models.ForeignKey('Pile', null=True)
    pile_position = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = 'scrap'
        verbose_name_plural = 'scraps'
        ordering = ('pile_position',)
    
    objects = ScrapManager()
    
    def __unicode__(self):
        return self.title or self.blueprint_name
    
    def data_load(self):
        return pickle.loads(str(self.data))
    
    def data_dump(self, data):
        self.data = pickle.dumps(data)
    
    def blueprint_display_name(self):
        for blueprint in Blueprint.inventory:
            if blueprint.name == self.blueprint_name:
                return blueprint.display_name
        return self.blueprint_name
    
    def prev_pile_position(self):
        if self.pile_position == 0:
            return 0
        return self.pile_position - 1

    def next_pile_position(self):
        return self.pile_position + 1

class PileManager(models.Manager):
    def standalone(self):
        return self.filter(is_standalone=True)


class Pile(models.Model):
    name = models.CharField(max_length=30)
    is_standalone = models.BooleanField(blank=False, default=True)
    is_enabled = models.BooleanField(default=True)
    
    objects = PileManager()
    
    def __unicode__(self):
        return self.name
    
    def scraps(self):
        return Scrap.objects.in_pile(self)
    
    def largest_scrap_position(self):
        if not self.scraps():
            return -1
        return self.scraps().aggregate(Max('pile_position'))['pile_position__max']

    def smallest_scrap_position(self):   
        if not self.scraps():
            return -1
        return self.scraps().aggregate(Min('pile_position'))['pile_position__min']
