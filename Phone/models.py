from enum import unique
from pyexpat import model
from django.db import models
from django.forms import SlugField
from django.utils.text import slugify


class ProcessorBrand(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    seo_title = models.CharField(max_length=70)
    seo_des = models.TextField(max_length=160)
    slug = models.SlugField(max_length=70, null=True, blank=True, unique=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProcessorBrand, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']