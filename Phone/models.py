from pyexpat import model
from django.db import models



class ProcessorBrand(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    seo_title = models.CharField(max_length=70)
    seo_des = models.TextField(max_length=160)
    #slug = slug = AutoSlugField(populate_from=('title',), unique=True, max_length=255, overwrite=True)


    def __str__(self):
        return self.name