from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from .models import GalleryImage, Phone, PhoneBrand, ProcessorBrand, Processor



class phone_brand_list(ListView):
    model = PhoneBrand
    template_name = 'phone/phone_brand.html'






def home(request):
    phone = Phone.objects.filter().order_by('-created')

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
        'brands':brands,
        'processor':processor
    }

    return render(request, 'processor/processor_list.html', context)




#Phone Filter by Status
def phone_filter(request, slug, status):
    brand=PhoneBrand.objects.get(slug=slug)
    phone=Phone.objects.filter(brand=brand, status=status)
    

    context = {
        'brand':brand,
        'phone':phone,
        'status':status,
    }

    return render(request, 'phone/phone_by_brand.html', context)


def phone_details(request, slug):
    phone = Phone.objects.get(slug=slug)

    context = {
        'phone':phone
    }

    return render(request, 'phone/phone_details.html', context)

def phone_gallery(request, slug):
    phone = Phone.objects.get(slug=slug)
    gallery = GalleryImage.objects.filter(phone=phone)
    

    context = {
        'phone':phone,
        'gallery':gallery,
    }

    return render(request, 'phone/phone_gallery.html', context)