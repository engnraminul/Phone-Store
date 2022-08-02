from django import views
from django.contrib import admin
from django.urls import path
from Phone import views 
app_name = 'Phone'
urlpatterns = [
    path('', views.ProcessorBrandList.as_view(), name='processor'),
    path('<slug>/', views.PrcessorDetail.as_view(), name='detail'),
]
