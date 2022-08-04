from distutils.command.upload import upload
from enum import unique
from pyexpat import model
from django.db import models
from django.forms import CharField, SlugField
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
        ordering = ['name']
        


class Processor(models.Model):
    brand = models.ForeignKey('ProcessorBrand', on_delete=models.PROTECT, related_name='Processor_Brand', null=True)
    title = models.CharField(max_length=100, blank=False, null=False, unique=True)
    chipset = models.CharField(max_length=120, blank=True, null=True)
    cpu = models.CharField(max_length=150, blank=True, null=True)
    gpu = models.CharField(max_length=50, blank=True, null=True)
    nm = models.CharField(max_length=20, blank=True, null=True)
    released = models.DateField()
    seo_title = models.CharField(max_length=70)
    seo_des = models.TextField(max_length=160)
    slug = models.SlugField(max_length=70, null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Processor, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering= ['-released']



class PhoneBrand(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to = 'brands')
    about = models.TextField(blank=True, null=True)
    seo_title = models.CharField(max_length=70)
    seo_des = models.TextField(max_length=160)
    slug = models.SlugField(max_length=70, null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PhoneBrand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering= ['name']
