from django.db import models
from django.utils.text import slugify
from tinymce import models as tinymce_models



class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name="Tilte")
    content = tinymce_models.HTMLField()
    image = models.ImageField(upload_to ='blog', null=False, blank=False)
    seo_title= models.CharField(max_length=80, blank=True, null=True)
    seo_des = models.TextField(blank=True, null=True)
    publish_date = models.DateField(auto_now_add=False)
    update_date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        ordering = ['publish_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)