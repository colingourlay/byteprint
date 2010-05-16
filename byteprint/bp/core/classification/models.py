from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

class ClassificationMappingManager(models.Manager):
    
    def get_for_object(self, obj):
        content_type = ContentType.objects.get_for_model(obj)
        return self.filter(content_type__pk=content_type.pk, object_id=obj.pk)

class ClassificationGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    plural_form = models.CharField(max_length=55, blank=True)
    adjective = models.CharField(max_length=55, blank=True)

    def __unicode__(self): 
        return self.name

    def plural(self):
        return self.plural_form or self.name + 's'

class Classification(models.Model):
    group = models.ForeignKey(ClassificationGroup)
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.name

class ClassificationMapping(models.Model):
    classification = models.ForeignKey(Classification, db_index=True)
    content_type = models.ForeignKey(ContentType, db_index=True)
    object_id = models.PositiveIntegerField(db_index=True)   
    object = generic.GenericForeignKey('content_type', 'object_id')

    objects = ClassificationMappingManager()

    def __unicode__(self):
        if self.group.adjective:
            return u'%s is %s as %s' % (
                self.object,
                self.group.adjective,
                self.classification)
        else:
            return u'%s is a member of the %s %s' % (
                self.object,
                self.classification,
                self.group)
    
    def group(self):
        return self.classification.group


