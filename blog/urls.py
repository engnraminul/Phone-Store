from turtle import title
from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path('list/', views.blog_list, name="blog_list"),
]