from codecs import charmap_build
from distutils.command.upload import upload
from email.mime import image
from enum import unique
from pyexpat import model
from django.db import models
from django.forms import CharField, SlugField
from django.utils.text import slugify
from django.utils.safestring import mark_safe


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
    brand = models.ForeignKey('ProcessorBrand', on_delete=models.PROTECT, related_name='Processor_Brand', null=True, blank=True)
    title = models.CharField(max_length=100, blank=False, null=False, unique=True)
    chipset = models.CharField(max_length=120, blank=True, null=True)
    cpu = models.CharField(max_length=150, blank=True, null=True)
    gpu = models.CharField(max_length=50, blank=True, null=True)
    nm = models.CharField(max_length=20, blank=True, null=True)
    released = models.DateField()
    seo_title = models.CharField(max_length=70)
    seo_des = models.TextField(max_length=None)
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
    published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PhoneBrand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering= ['name']



class Phone(models.Model):
    STATUS = (
        ("Released", "Released"),
        ("Upcoming","Upcoming"),
        ("Rumor", "Rumor"),
        ("Draft", "Draft"),
    )
    #Basic Informations
    name = models.CharField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    brand = models.ForeignKey(PhoneBrand, related_name="phone_brand", on_delete=models.PROTECT, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Released')
    annoucement = models.DateField(null=True, blank=True)
    release = models.DateField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)
    price = models.IntegerField(null=True, blank=True)
    old_price = models.IntegerField(null=True, blank=True)

    #Network
    network_type = models.CharField(max_length=100, null=True, blank=True)
    network_speed = models.CharField(max_length=100, null=True, blank=True)
    sim = models.CharField(max_length=50, null=True, blank=True)
    two_g= models.BooleanField(default=True)
    two_g_band = models.CharField(max_length=100, null=True, blank=True)
    three_g =models.BooleanField(default=True)
    three_g_band = models.CharField(max_length=100, null=True, blank=True)
    four_g = models.BooleanField(default=False)
    four_g_band = models.CharField(max_length=100, null=True, blank=True)
    five_g = models.BooleanField(default=False)
    five_g_band = models.CharField(max_length=100, null=True, blank=True)
    six_g = models.BooleanField(default=False)
    six_g_band = models.CharField(max_length=100, null=True, blank=True)
    seven_g = models.BooleanField(default=False)
    seven_g_band = models.CharField(max_length=100, null=True, blank=True)

    #Body
    dimension = models.CharField(max_length=100, null=True, blank=True)
    weight = models.CharField(max_length=20, null=True, blank=True)
    front = models.CharField(max_length=50, null=True, blank=True)
    back = models.CharField(max_length=50, null=True, blank=True)
    frame = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    body_feature = models.TextField(null=True, blank=True)

    #Display
    display_type = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=20, null=True, blank=True)
    resulation = models.CharField(max_length=50, null=True, blank=True)
    ratio = models.CharField(max_length=20, null=True, blank=True)
    pixel_density = models.CharField(max_length=20, null=True, blank=True)
    refresh_rate = models.CharField(max_length=20, null=True, blank=True)
    protection = models.CharField(max_length=100, null=True, blank=True)
    display_features = models.TextField(max_length=None, null=True, blank=True)
    second_display = models.TextField(max_length=200, null=True, blank=True)

    #camera
    back_camera = models.TextField(max_length=None, null=True, blank=True)
    back_camera_features = models.CharField(max_length=150, null=True, blank=True)
    back_camera_video = models.CharField(max_length=150, null=True, blank=True)

    front_camera = models.TextField(max_length=None, null=True, blank=True)
    front_camera_features = models.CharField(max_length=150, null=True, blank=True)
    front_camera_video = models.CharField(max_length=150, null=True, blank=True)

    #platform
    os = models.CharField(max_length=50, null=True, blank=True)
    os_version = models.CharField(max_length=50, null=True, blank=True)
    ui = models.CharField(max_length=50, null=True, blank=True)
    processor = models.ForeignKey(Processor, related_name="phone_processor", on_delete=models.PROTECT, null=True, blank=True)
    chipset = models.TextField(max_length=None, null=True, blank=True)


    #Memory
    ram = models.CharField(max_length=100, null=True, blank=True)
    storage = models.CharField(max_length=100, null=True, blank=True)
    memory_slot = models.BooleanField(default=False, null=True, blank=True)
    variant = models.CharField(max_length=50, null=True, blank=True)
    storage_type = models.CharField(max_length=50, null=True, blank=True)

    #Audio
    speaker = models.CharField(max_length=100, null=True, blank=True)
    audio_jack = models.BooleanField(default=False)
    audio_features = models.CharField(max_length=100, null=True, blank=True)

    #Connectivity
    wifi = models.CharField(max_length=100, null=True, blank=True)
    hotspot = models.BooleanField(default=True)
    nfc = models.BooleanField(default=False)
    gps = models.BooleanField(default=True)
    radio = models.BooleanField(default=True)
    usb = models.CharField(max_length=100, null=True, blank=True)
    infrared_port = models.BooleanField(default=False)

    #Sensor
    fingureprint = models.CharField(max_length=100, null=True, blank=True)
    facelock = models.CharField(max_length=100, null=True, blank=True)
    sensor = models.CharField(max_length=200, null=True, blank=True)

    #Battery
    battery_type = models.CharField(max_length=100, null=True, blank=True)
    battery_capacity = models.CharField(max_length=50, null=True, blank=True)
    charging = models.CharField(max_length=100, null=True, blank=True)
    wireless_charging = models.CharField(max_length=100, null=True, blank=True)
    reverse_charging = models.CharField(max_length=100, null=True, blank=True)
    charging_features = models.TextField(max_length=None, null=True, blank=True)

    #Price
    united_states = models.TextField(max_length=None, null=True, blank=True)
    europe = models.TextField(max_length=None, null=True, blank=True)
    china = models.TextField(max_length=None, null=True, blank=True)
    india = models.TextField(max_length=None, null=True, blank=True)


    #Images
    thumbnail = models.ImageField(upload_to = 'phone', null=True)

    #Seo
    seo_title = models.CharField(max_length=70, null=True, blank=True)
    seo_des = models.TextField(max_length=170, null=True, blank=True)
    slug = models.CharField(max_length=70, unique=True, null=True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering= ['-created']

    #Admin List display Show Image
    def admin_photo(self):
        return mark_safe('<img src="{}" width="50" />'.format(self.thumbnail.url))
    admin_photo.short_description = 'Thumbnail'
    admin_photo.allow_tags =True

class GalleryImage(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    images = models.FileField(upload_to= 'phone', null=True, blank=True)
    
    
