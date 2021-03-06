from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    cat_max_length = 128
    name = models.CharField(max_length=cat_max_length, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

class Page(models.Model):
    page_max_length = 128
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=page_max_length)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    # required to link UserProfile to User Model instance.
    user = models.OneToOneField(User)

    # additional attributes to include
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # override the __unicode__ method
    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username


