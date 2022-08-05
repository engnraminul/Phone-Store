from django.contrib import admin
from .models import GalleryImage, ProcessorBrand, Processor, PhoneBrand, Phone


class GalleryImageAdmin(admin.StackedInline):
    model = GalleryImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryImageAdmin]
    #prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'model', 'brand', 'category', 'status', 'annoucement', 'release', 'created',),

        }),
        ('Network', {
            'fields': ('network_type', 'network_speed', 'sim', 'two_g', 'two_g_band', 'three_g', 'three_g_band', 'four_g', 'four_g_band', 'five_g', 'five_g_band', 'six_g', 'six_g_band', 'seven_g', 'seven_g_band', ),

        }),
    )

admin.site.register(ProcessorBrand)
admin.site.register(Processor)
admin.site.register(PhoneBrand)
admin.site.register(Phone, ProductAdmin)