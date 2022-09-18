from atexit import register
from django import template

from Phone.models import PhoneBrand

register = template.Library()

@register.filter
def brand_tags(request):
    if request:
        brand_tags = PhoneBrand.objects.filter(published=True).order_by('id')
        return brand_tags
