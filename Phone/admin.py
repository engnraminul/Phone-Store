from django.contrib import admin
from .models import GalleryImage, ProcessorBrand, Processor, PhoneBrand, Phone


class GalleryImageAdmin(admin.StackedInline):
    model = GalleryImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryImageAdmin]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(ProcessorBrand)
admin.site.register(Processor)
admin.site.register(PhoneBrand)
admin.site.register(Phone, ProductAdmin)