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


def ProcessorList(request, slug, id):

    processor_list = Processor.objects.filter(brand_id = id)
    brand = ProcessorBrand.objects.get(id = id)
    brand.Processor_Brand.all()

    
    
    context={
        'processor_list':processor_list,
        'brand':brand,
        }

    return render(request, 'processor/processor_list.html', context )