from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from .models import Phone, PhoneBrand, ProcessorBrand, Processor


# class ProcessorBrandList(ListView):
#     model = ProcessorBrand
#     template_name = 'processor/brand.html'


class phone_brand_list(ListView):
    model = PhoneBrand
    template_name = 'phone/phone_brand.html'



def ProcessorList(request, slug):
    brands=ProcessorBrand.objects.get(slug=slug)
    all_processor=Processor.objects.filter(brand=brands)
    #print(all_processor)

    context={
        "brand":brands,
        "all_processor":all_processor,
    }
    
    return render(request, 'processor/processor_list.html', context)

def home(request):
    phone = Phone.objects.filter()


    context = {
        'phone': phone
    }

    return render(request, 'home.html', context)



def phone_by_processor(request, slug):
    processor = Processor.objects.get(slug=slug)
    phone = Phone.objects.filter(processor=processor, status='Released')

    context = {
        'processor':processor,
        'phone':phone
    }

    return render(request, 'phone/phone_by_processor.html', context)




def Processor_by_brand(request, slug):
    brand=ProcessorBrand.objects.all()
    brands = ProcessorBrand.objects.get(slug=slug)
    processor=Processor.objects.filter(brand=brands)
    

    context = {
        'brand':brand,
        'processor':processor
    }

    return render(request, 'processor/processor_list.html', context)



def phone_by_brand(request,slug):
    phonebrand=PhoneBrand.objects.get(slug=slug)
    phone=Phone.objects.filter(brand=phonebrand, status='Released')
    

    context = {
        'brand':phonebrand,
        'phone':phone,
    }

    return render(request, 'phone/phone_by_brand.html', context)

#Phone Filter by Status
def phone_filter(request, slug, status):
    phonebrand=PhoneBrand.objects.get(slug=slug)
    phone=Phone.objects.filter(brand=phonebrand, status=status)
    

    context = {
        'brand':phonebrand,
        'phone':phone
    }

    return render(request, 'phone/phone_by_brand.html', context)