from multiprocessing import context
from django.shortcuts import render
from .models import *

def blog_list(request):
    blog = Blog.objects.all()
    print(blog)

    context = {
        'blog':blog,
    }
    return render(request, 'blog/blog_list.html', context)
