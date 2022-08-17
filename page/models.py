from django.db import models
from django.utils.text import slugify
from django.utils.safestring import mark_safe



class Page(models.Model):
    page_title = models.CharField(max_length=250, verbose_name="Tilte")
    page_content = models.TextField(verbose_name="Content")
    slug = models.SlugField(max_length=250, unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.page_title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.page_title)
        super(Page, self).save(*args, **kwargs)