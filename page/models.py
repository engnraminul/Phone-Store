from django.db import models
from django.utils.text import slugify
from tinymce import models as tinymce_models



class Page(models.Model):
    title = models.CharField(max_length=250, verbose_name="Tilte")
    content = tinymce_models.HTMLField()
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)