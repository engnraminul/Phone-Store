from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import ListView
from .models import GalleryImage, Phone, PhoneBrand, ProcessorBrand, Processor
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator





class phone_brand_list(ListView):
    model = PhoneBrand
    template_name = 'phone/phone_brand.html'






def home(request):
    phone = Phone.objects.filter(status='Released').order_by('-created')[:12]
    u_phone= Phone.objects.filter(status='Upcoming').order_by('-created')[:8]
    
    


    context = {
        'u_phone': u_phone,
        'phone': phone,
        
    }
    return render(request, 'home.html', context)



def phone_by_processor(request, slug):
    processor = Processor.objects.get(slug=slug)
    phone = Phone.objects.filter(processor=processor, status='Released')
    paginator = Paginator(phone, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj,
        'processor':processor,
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
    brand_phone = Phone.objects.filter(brand=phone.brand,)[:6]

    context = {
        'phone':phone,
        'brand_phone':brand_phone,
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



def search_result(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        res = None
        phone = request.POST.get('phone')
        query_s= Phone.objects.filter(name__icontains=phone)[:5]
        if len(query_s) > 0 and len(phone) > 0:
            data = []
            for pos in query_s:
                item = {
                    'slug':pos.slug,
                    'name':pos.name,
                    'thumbnail':str(pos.thumbnail.url),
                    'status':pos.status,
                }
                data.append(item)
            
            res = data
        else:
            res = 'Phone not found'
        return JsonResponse({'data':res})
    
    return JsonResponse({})



def phone_list(request, status):
    
    phone = Phone.objects.filter(status=status)
    paginator = Paginator(phone, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj,
        'status':status,
    }

    return render(request, 'phone/phone_list.html', context)


def phone_by_category(request, category):
    
    phone = Phone.objects.filter(category=category)
    paginator = Paginator(phone, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj,
        'category':category,
    }

    return render(request, 'phone/phone_by_category.html', context)


class Compare(TemplateView):
    def get(self, request, *args, **kwargs):
        phonelist = Phone.objects.all()

        context = {
            'phonelist':phonelist,
            
        }
        return render(request, 'phone/compare.html', context)

    def post(self, request, *args, **kwargs):
        if request.method =='POST' or request.method == 'post':
            compare_1 = request.POST.get('phone1')
            compare_2 = request.POST.get('phone2')
            
            print(compare_1)
            print("print..............................")
            phone1 = Phone.objects.get(name=compare_1)
            phone2 = Phone.objects.get(name=compare_2)
            

            context = {
                'phone':phone1,
                'phone2':phone2,
                
                    
                }
            return render(request, 'phone/compare.html', context)
            