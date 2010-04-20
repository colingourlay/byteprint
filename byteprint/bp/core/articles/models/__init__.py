import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe

from bp.contrib.autoslug.fields import AutoSlugField
from bp.core.config.models import Setting
from bp.core.scraps.models import Pile

def are_comments_enabled_by_default():
    return Setting.objects.get_boolean("article_comments_enabled_by_default")

class ArticleManager(models.Manager):
    
    def articles(self):
        return self.filter(is_page=False)
        
    def published_articles(self):
        return self.filter(is_published=True, is_page=False)
 
    def latest_published_articles(self, count=1):
        return self.filter(is_published=True, is_page=False).order_by('-created')[:count]

    def pages(self):
        return self.filter(is_page=True)
        
    def published_pages(self):
        return self.filter(is_published=True, is_page=True)

class Article(models.Model):
    title = models.TextField()
    slug = AutoSlugField(populate_from='title', unique_with='created__month', always_update=True)
    author = models.ForeignKey(User)
    pile = models.ForeignKey(Pile)
    rendered_pile = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now_add=True, verbose_name='date_updated')
    created = models.DateTimeField(auto_now_add=True, verbose_name='date_created')
    is_published = models.BooleanField(default=False)
    is_page = models.BooleanField(default=False)
    enable_comments = models.BooleanField()
    show_comments = models.BooleanField(default=True)
    
    objects = ArticleManager()
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.enable_comments = are_comments_enabled_by_default()
        super(Article, self).save(*args, **kwargs)
    
    @permalink
    def get_absolute_url(self):
        if self.is_page:
            return ('articles_public_page_detail', (), {'slug': self.slug})
        else: 
            return ('articles_public_article_detail', (), {
                'year': self.created.year,
                'month': self.created.month,
                'slug': self.slug})
    
    def body(self):
        return mark_safe(self.rendered_pile)