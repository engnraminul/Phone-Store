from django import views
from django.contrib import admin
from django.urls import path, include
from StoreMain import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('processor', include('Phone.urls')),
    path('', views.index, name="index"),
]
