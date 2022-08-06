from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from .models import Phone, PhoneBrand, ProcessorBrand, Processor


class ProcessorBrandList(ListView):
    model = ProcessorBrand
    template_name = 'processor/brand.html'


# class PhoneBrandList(ListView):
#     model = PhoneBrand
#     template_name = 'phone/phone_brand.html'

def PhoneBrandList(request):
    brandlist = PhoneBrand.objects.all()

    context = {
        'brandlist': brandlist
    }

    return render(request, 'phone/phone_brand.html', context)



def ProcessorList(request, slug):
    brands=ProcessorBrand.objects.get(slug=slug)
    all_processor=Processor.objects.filter(brand=brands)
    print(all_processor)

    context={
        "brand":brands,
        "all_processor":all_processor,
    }
    
    return render(request, 'processor/processor_list.html', context)

def home(request):
    phone = Phone.objects.filter(status = 'Released')


    context = {
        'phone': phone
    }

    return render(request, 'home.html', context)