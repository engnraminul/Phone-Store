from atexit import register
from django import template

from Phone.models import PhoneBrand

register = template.Library()

@register.simple_tag(takes_context=True, name='phone_brand')
def phone_brand():
    brand=PhoneBrand.objects.all()
    return brand
