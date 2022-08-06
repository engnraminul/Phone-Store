from django.contrib import admin
from .models import GalleryImage, ProcessorBrand, Processor, PhoneBrand, Phone

#Phone Clone
def clone(modeladmin, request, queryset):
        for object in queryset:
            object.id = None
            object.status = 'Draft'
            object.name ='(clone) ' + object.name
            object.save()
clone.short_description = "Clone"



class GalleryImageAdmin(admin.StackedInline):
    model = GalleryImage
#phone model fieldset
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryImageAdmin]
    list_display = ('name', 'brand', 'status', 'created', 'admin_photo',)
    list_filter = ('brand', 'processor', 'status',)
    search_fields = ('name',)
    actions = [clone]
    
    #prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Basic', {
            'fields': ('name', 'model', 'brand', 'category', 'status', 'annoucement', 'release', 'created', 'thumbnail',),

        }),

        ('Network', {
            'fields': ('network_type', 'network_speed', 'sim', 'two_g', 'two_g_band', 'three_g', 'three_g_band', 'four_g', 'four_g_band', 'five_g', 'five_g_band', 'six_g', 'six_g_band', 'seven_g', 'seven_g_band', ),

        }),

        ('Body', {
            'fields': ('dimension', 'weight', 'front', 'back', 'frame', 'color', 'body_feature',),

        }),

        ('Display', {
            'fields': ('display_type', 'size', 'resulation', 'ratio', 'pixel_density', 'refresh_rate', 'protection', 'display_features', 'second_display',),

        }),

        ('Camera', {
            'fields': ('back_camera', 'back_camera_features', 'back_camera_video',  'front_camera', 'front_camera_features', 'front_camera_video',),

        }),

        ('Platform', {
            'fields': ('os', 'os_version', 'ui', 'processor', 'chipset', ),

        }),

        ('Memory', {
            'fields': ('ram', 'storage', 'memory_slot', 'variant', 'storage_type', ),

        }),

        ('Audio', {
            'fields': ('speaker', 'audio_jack', 'audio_features',),

        }),

        ('Connectivity', {
            'fields': ('wifi', 'hotspot', 'nfc', 'gps', 'radio', 'usb', 'infrared_port',),

        }),

        ('Sensor', {
            'fields': ('fingureprint', 'facelock', 'sensor',),

        }),

        ('Battery', {
            'fields': ('battery_type', 'battery_capacity', 'charging', 'wireless_charging', 'reverse_charging', 'charging_features',),

        }),

        ('Price', {
            'fields': ('united_states', 'europe', 'china', 'india',),

        }),

        ('Seo', {
            'fields': ('seo_title', 'seo_des', 'slug',),

        }),

        
    )

admin.site.register(ProcessorBrand)
admin.site.register(Processor)
admin.site.register(PhoneBrand)
admin.site.register(Phone, ProductAdmin)