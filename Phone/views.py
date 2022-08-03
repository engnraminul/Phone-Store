from unicodedata import name
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from .models import ProcessorBrand, Processor


class ProcessorBrandList(ListView):
    model = ProcessorBrand
    template_name = 'processor/brand.html'


# class ProcessorList(ListView):
#     model = Processor
#     template_name = 'processor/processor_list.html'


def ProcessorList(request, id, slug):
    #processor_list = Processor.objects.all()
    #brand_id = request.GET.get('brandid')

  
    processor_list = Processor.objects.filter(brand_id = id)
    
    
    context={
        'processor_list':processor_list
        }

    return render(request, 'processor/processor_list.html', context )