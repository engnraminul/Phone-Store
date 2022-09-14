from django.db import models
from django.utils.text import slugify
from tinymce import models as tinymce_models
from Phone.models import Phone
from django.urls import reverse



class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name="Tilte")
    content = tinymce_models.HTMLField()
    image = models.ImageField(upload_to ='blog', null=True, blank=True)
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
    
    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"title":self.slug})


class Top10(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to ='blog', null=False, blank=False)
    phone1=models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='phone1', null=True, blank=True)
    phone2=models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='phone2', null=True, blank=True)
    phone3=models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='phone3', null=True, blank=True)
    phone4=models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='phone4', null=True, blank=True)
    phone5=models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='phone5', null=True, blank=True)
    phone6=models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='phone6', null=True, blank=True)
    phone7=models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='phone7', null=True, blank=True)
    phone8=models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='phone8', null=True, blank=True)
    phone9=models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='phone9', null=True, blank=True)
    phone10=models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='phone10', null=True, blank=True)
    publish_date = models.DateField(auto_now_add=False)
    seo_title= models.CharField(max_length=80, blank=True, null=True)
    seo_des = models.TextField(max_length=170,blank=True, null=True)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    published = models.BooleanField(default=True)


    class Meta:
        ordering = ['publish_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Top10, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("blog:top10_detail", kwargs={"slug":self.slug})


