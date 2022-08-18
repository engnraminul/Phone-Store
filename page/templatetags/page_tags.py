from atexit import register
from django import template

from page.models import Page

register = template.Library()

@register.filter
def page_tags(request):
    if request:
        page_tags = Page.objects.all()
        return page_tags