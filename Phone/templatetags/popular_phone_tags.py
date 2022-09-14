from atexit import register
from django import template

from Phone.models import Phone

register = template.Library()

@register.filter
def popular_tags(request):
    if request:
        popular_tags = Phone.objects.filter(status='Released').order_by('-views')[:10]
        return popular_tags


@register.filter
def upcoming_popular_tags(request):
    if request:
        upcoming_popular_tags = Phone.objects.filter(status='Upcoming').order_by('-views')[:10]
        return upcoming_popular_tags