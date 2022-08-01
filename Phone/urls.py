from django import views
from django.contrib import admin
from django.urls import path
from Phone import views 

urlpatterns = [
    path('', views.ProcessorBrandList.as_view(), name='processor'),
]
