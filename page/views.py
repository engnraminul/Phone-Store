from multiprocessing import context
from django.shortcuts import render
from .models import Page


def page_detail(request, slug):

    page = Page.objects.get(slug=slug)

    context = { 
        'page':page
    }

    return render(request, 'page_detail.html', context)
