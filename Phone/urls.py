from django import views
from django.urls import path
from Phone import views 
from django.contrib.sitemaps.views import sitemap
from Phone.sitemap import PhoneSitemap, PhoneBrandSitemap, ProcessorBrandSitemap, PhoneProcessorSitemap, GallerySitemap

app_name = 'Phone'


sitemaps = {
		"phone": PhoneSitemap,
}

phonebrandsitemaps = {
		"phonebrand": PhoneBrandSitemap,
}

phonebrandsitemaps = {
		"processorbrand": ProcessorBrandSitemap,
}

phoneprocessorsitemaps = {
		"phoneprocessor": PhoneProcessorSitemap,
}

imagegallerysitemaps = {
		"imagegallery": GallerySitemap,
}
urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('phonebrand_sitemap.xml', sitemap, {'sitemaps': phonebrandsitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('processorbrand_sitemap.xml', sitemap, {'sitemaps': phonebrandsitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('phoneprocessor_sitemap.xml', sitemap, {'sitemaps': phoneprocessorsitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('imagegallery_sitemap.xml', sitemap, {'sitemaps': imagegallerysitemaps}, name='django.contrib.sitemaps.views.sitemap'),
                
    
    path('compare', views.Compare.as_view(), name="compare"),
    path('<slug>', views.phone_details, name="phone_details"),
    path('', views.home, name= "home"),
    path('<brand>/', views.phone_brand_list, name="phone_brand_list"),
    path('phone/search/', views.search_result, name="search"),
    path('<slug>/processor/', views.Processor_by_brand, name="Processor_by_brand" ),
    path('phone/<slug>/', views.phone_by_processor, name="phone_by_processor"),
    path('<slug>/<status>', views.phone_filter, name="phone_filter"),
    path('<slug>/images/', views.phone_gallery, name="phone_gallery"),
    path('phones/<status>/', views.phone_list, name="phone_list"),
    path('category/<category>/', views.phone_by_category, name="phone_by_category"),
    
    
    
    
    
    
    
    
    
    

]



    # path('', views.home, name= "home"),
    # path('<slug>', views.Processor_by_brand, name="Processor_by_brand" ),
    # path('brand/', views.phone_brand_list.as_view(), name="phone_brand_list"),
    # path('<slug>/<status>/', views.phone_filter, name="phone_filter"),
    # path('phone/<slug>', views.phone_by_processor, name="phone_by_processor"),
    # path('<slug>/', views.phone_details, name="phone_details"),
    # path('images/<slug>', views.phone_gallery, name="phone_gallery"),
    