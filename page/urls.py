from django.urls import path
from page import views


app_name = 'page'

urlpatterns = [
    path('<slug>/', views.page_detail, name='page_detail'),
]
