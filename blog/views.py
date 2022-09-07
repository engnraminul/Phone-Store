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


def top10_list(request):
    top10 = Top10.objects.all()
    paginator = Paginator(top10, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj,
    }
    return render(request, 'blog/top10_list.html', context)


def top10_detail(request, slug):
    top10 = Top10.objects.filter(slug=slug)

    context = {
        'top10':top10,
    }

    return render(request, 'blog/top10_detail.html', context)
