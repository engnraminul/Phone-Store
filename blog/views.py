from multiprocessing import context
from django.shortcuts import render
from .models import *

def blog_list(request):
    blog = Blog.objects.all()

    context = {
        'blog':blog,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, title):
    blog = Blog.objects.filter(slug=title)

    context = {
        'blog':blog,
    }

    return render(request, 'blog/blog_detail.html', context)