from turtle import title
from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path('list/', views.blog_list, name="blog_list"),
    path('details/<title>', views.blog_detail, name="blog_detail"),
    path('top10/', views.top10_list, name='top10'),
    path('top10/details/<slug>/', views.top10_detail, name='top10_detail'),
]