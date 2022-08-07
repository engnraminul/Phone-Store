from django import views
from django.contrib import admin
from django.urls import path
from Phone import views 

app_name = 'Phone'

urlpatterns = [
    path('', views.home, name= "home"),
    path('processor', views.ProcessorBrandList.as_view(), name='processor'),
    path('<slug>/', views.Processor_by_brand, name="Processor_by_brand" ),
    path('brand/', views.PhoneBrandList, name="phone_brand_list"),
    path('<slug>/', views.phone_by_brand, name="phone_by_brand"),
    path('<slug>/<status>/', views.phone_filter, name="phone_filter"),
    path('phone/<slug>', views.phone_by_processor, name="phone_by_processor"),
    
]
