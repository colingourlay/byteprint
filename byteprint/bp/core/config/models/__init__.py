from django.db import models

class SettingManager(models.Manager):
    def add(self, key, value, is_templatable=False):
        definition = self.model(None, key, value, is_templatable)
        definition.save()
        return definition
    
    def add_templatable(self, key, value):
        definition = self.model(None, key, value, True)
        definition.save()
        return definition
    
    def get_value(self, key):
        setting = self.get(key=key) or None
        if setting:
            return setting.value
        return None
    
    def get_boolean(self, key):
        value = self.get_value(key)
        if len(value) > 0:
            return True
        return False
    
    def templatable(self):
        return self.filter(is_templatable=True)

class Setting(models.Model):
    key = models.CharField(max_length=40)
    value = models.TextField(blank=True)
    is_templatable = models.BooleanField()
    
    objects = SettingManager()

    class Meta:
        verbose_name = 'setting'
        verbose_name_plural = 'settings'

    def __unicode__(self):
        return self.key