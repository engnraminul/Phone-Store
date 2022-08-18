from django import views
from django.urls import path
from Phone import views 

app_name = 'Phone'

urlpatterns = [
    path('', views.home, name= "home"),
    #path('processor', views.ProcessorBrandList.as_view(), name='processor'),
    path('<slug>', views.Processor_by_brand, name="Processor_by_brand" ),
    path('brand/', views.phone_brand_list.as_view(), name="phone_brand_list"),
    path('<slug>/<status>/', views.phone_filter, name="phone_filter"),
    path('phone/<slug>', views.phone_by_processor, name="phone_by_processor"),
    path('<slug>/', views.phone_details, name="phone_details"),
    path('images/<slug>', views.phone_gallery, name="phone_gallery"),
    
]
