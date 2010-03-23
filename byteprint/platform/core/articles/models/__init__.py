import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify

from platform.contrib.autoslug.fields import AutoSlugField

from platform.core.config.models import Setting
from platform.core.scraps.models import Pile

def are_comments_enabled_by_default():
    return Setting.objects.get_boolean("article_comments_enabled_by_default")

class ArticleManager(models.Manager):
    def are_published(self):
        return self.filter(publish=True, published__lte=datetime.datetime.now())
    

class Article(models.Model):
    title = models.TextField()
    slug = AutoSlugField(populate_from='title', unique_with='published__month', always_update=True)
    body = models.TextField(blank=True)
    author = models.ForeignKey(User)
    #pile = models.ForeignKey(Pile)
    created = models.DateTimeField(auto_now_add=True, verbose_name='date_created')
    updated = models.DateTimeField(auto_now=True, verbose_name='date_updated')
    published = models.DateTimeField(auto_now_add=True, verbose_name='date_published')
    publish = models.BooleanField(default=False)
    enable_comments = models.BooleanField()
    show_comments = models.BooleanField(default=True)
    
    objects = ArticleManager()
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if not self.id:
            self.enable_comments = are_comments_enabled_by_default()
        super(Article, self).save(*args, **kwargs)
    
    @permalink
    def get_absolute_url(self):
        return ('articles_public_article_detail', (), {
            'year': self.published.year,
            'month': self.published.month,
            'slug': self.slug})
    
    def is_published(self):
        return self.publish and self.published <= datetime.datetime.now()