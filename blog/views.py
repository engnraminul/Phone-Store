import imp
from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

def blog_list(request):
    blog = Blog.objects.all()
    paginator = Paginator(blog, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, title):
    blog = Blog.objects.filter(slug=title)

    context = {
        'blog':blog,
    }

    return render(request, 'blog/blog_detail.html', context)