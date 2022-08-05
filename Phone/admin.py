from django.contrib import admin
from .models import ProcessorBrand, Processor, PhoneBrand, Phone

admin.site.register(ProcessorBrand)
admin.site.register(Processor)
admin.site.register(PhoneBrand)
admin.site.register(Phone)