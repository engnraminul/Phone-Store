from django.contrib import admin
from .models import ProcessorBrand, Processor, PhoneBrand

admin.site.register(ProcessorBrand)
admin.site.register(Processor)
admin.site.register(PhoneBrand)