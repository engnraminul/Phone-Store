from codecs import charmap_build
from distutils.command.upload import upload
from enum import unique
from platform import platform
from pyexpat import model
from turtle import color
from unicodedata import category
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
    model = models.CharField(max_length=50)
    brand = models.ForeignKey(PhoneBrand, on_delete=models.PROTECT, null=True, blank=True)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS)
    annoucement = models.DateField()
    release = models.DateField()

    #Network
    network_type = models.CharField(max_length=100)
    network_speed = models.CharField(max_length=100)
    sim = models.CharField(max_length=50)
    two_g= models.BooleanField(default=True)
    two_g_band = models.CharField(max_length=100)
    three_g =models.BooleanField(default=True)
    three_g_band = models.CharField(max_length=100)
    four_g = models.BooleanField(default=False)
    four_g_band = models.CharField(max_length=100)
    five_g = models.BooleanField(default=False)
    five_g_band = models.CharField(max_length=100)
    six_g = models.BooleanField(default=False)
    six_g_band = models.CharField(max_length=100)
    seven_g = models.BooleanField(default=True)
    seven_g_band = models.CharField(max_length=100)

    #Body
    dimension = models.CharField(max_length=100)
    weight = models.CharField(max_length=20)
    front = models.CharField(max_length=50)
    back = models.CharField(max_length=50)
    frame = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    body_feature = models.TextField()

    #Display
    display_type = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    resulation = models.CharField(max_length=50)
    ratio = models.CharField(max_length=20)
    pixel_density = models.CharField(max_length=20)
    refresh_rate = models.CharField(max_length=20)
    protection = models.CharField(max_length=100)
    display_features = models.CharField(max_length=100)

    #camera
    back_camera = models.TextField(max_length=None)
    back_camera_features = models.CharField(max_length=150)
    back_camera_video = models.CharField(max_length=150)

    front_camera = models.TextField(max_length=None)
    front_camera_features = models.CharField(max_length=150)
    front_camera_video = models.CharField(max_length=150)

    #platform
    os = models.CharField(max_length=50)
    os_version = models.CharField(max_length=50)
    ui = models.CharField(max_length=50)
    processor = models.ForeignKey(Processor, on_delete=models.PROTECT, null=True, blank=True)
    chipset = models.TextField(max_length=None)


    #Memory
    ram = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    memory_slot = models.BooleanField(default=False)
    variant = models.CharField(max_length=50)
    storage_type = models.CharField(max_length=50)

    #Audio
    speaker = models.CharField(max_length=100)
    audio_jack = models.BooleanField(default=False)
    audio_features = models.CharField(max_length=100)

    #Connectivity
    wifi = models.CharField(max_length=100)
    hotspot = models.BooleanField(default=True)
    nfc = models.BooleanField(default=False)
    gps = models.BooleanField(default=True)
    radio = models.BooleanField(default=True)
    usb = models.CharField(max_length=100)
    infrared_port = models.BooleanField(default=False)

    #Sensor
    fingureprint = models.CharField(max_length=100)
    facelock = models.CharField(max_length=100)
    sensor = models.CharField(max_length=200)

    #Battery
    battery_type = models.CharField(max_length=100)
    battery_capacity = models.CharField(max_length=50)
    charging = models.CharField(max_length=100)
    wireless_charging = models.CharField(max_length=100)
    reverse_charging = models.CharField(max_length=100)
    charging_features = models.TextField(max_length=None)

    #Price
    united_states = models.TextField(max_length=None)
    europe = models.TextField(max_length=None)
    india = models.TextField(max_length=None)
