from atexit import register
from django import template

from blog.models import Top10

register = template.Library()

@register.filter
def top10_tags(request):
    if request:
        top10_tags = Top10.objects.filter(published=True).order_by('-publish_date')[:5]
        return top10_tags
