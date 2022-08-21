from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import ListView
from .models import GalleryImage, Phone, PhoneBrand, ProcessorBrand, Processor
from django.http import JsonResponse
from django.db.models import Q




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
    #processor = get_object_or_404(Processor, slug=slug)
    phone = Phone.objects.filter(processor=processor, status='Released')

    context = {
        'processor':processor,
        'phone':phone
    }

    return render(request, 'phone/phone_by_processor.html', context)




def Processor_by_brand(request, slug):
    brand=ProcessorBrand.objects.all()
    #brands = get_object_or_404(ProcessorBrand, slug=slug)
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
    #brand = get_object_or_404(PhoneBrand, slug=slug)
    phone=Phone.objects.filter(brand=brand, status=status)
    

    context = {
        'brand':brand,
        'phone':phone,
        'status':status,
    }

    return render(request, 'phone/phone_by_brand.html', context)


def phone_details(request, slug):
    phone = Phone.objects.get(slug=slug)
    #phone = get_object_or_404(Phone, slug=slug)

    context = {
        'phone':phone
    }

    return render(request, 'phone/phone_details.html', context)


def phone_gallery(request, slug):
    phone = Phone.objects.get(slug=slug)
    #phone = get_object_or_404(Phone, slug=slug)
    gallery = GalleryImage.objects.filter(phone=phone)
    

    context = {
        'phone':phone,
        'gallery':gallery,
    }

    return render(request, 'phone/phone_gallery.html', context)

# def is_ajax(request):
#     return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# def search_results(request):
#     if is_ajax(request):
#         res = None
#         phone = request.POST.get('phone')
#         qs = Phone.objects.filter(name_icontains=phone)
#         if len(qs) > 0 and len(phone) > 0:
#             data = []
#             for pos in qs:
#                 item = {
#                     'slug':pos.slug,
#                     'name':pos.name,
#                     'thumbnail':pos.thumbnail,
#                 }
#                 data.append(item)
            
#             res = data
        
#         else:
#             res = 'Phone not found!'
#         return JsonResponse({'data':res})
    
#     return JsonResponse({})




def search_result(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        res = None
        phone = request.POST.get('phone')
        query_s= Phone.objects.filter(Q(name__icontains=phone))
        if len(query_s) > 0 and len(phone) > 0:
            data = []
            for pos in query_s:
                item = {
                    'slug':pos.slug,
                    'name':pos.name,
                    'thumbnail':str(pos.thumbnail.url),
                }
                data.append(item)
            
            res = data
        else:
            res = 'Phone not found'
        return JsonResponse({'data':res})
    
    return JsonResponse({})

