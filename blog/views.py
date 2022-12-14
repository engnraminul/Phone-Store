from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
import datetime

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
    blog = Blog.objects.get(slug=title)
    currentdate = datetime.date.today()
    date = currentdate.strftime("%B, %Y")

    context = {
        'blog':blog,
        'date':date,
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
    top10 = Top10.objects.get(slug=slug)
    currentdate = datetime.date.today()
    date = currentdate.strftime("%B, %Y")

    context = {
        'phone':top10,
        'date':date,
    }

    return render(request, 'blog/top10_detail.html', context)
