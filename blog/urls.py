from django.urls import path
from blog import views
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import BlogSitemap, Top10Sitemap


app_name = 'blog'

blog_itemaps = {
		"blog": BlogSitemap,
}

top10_itemaps = {
		"blog": Top10Sitemap,
}

urlpatterns = [
    path('postsitemap.xml', sitemap, {'sitemaps': blog_itemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('top10sitemap.xml', sitemap, {'sitemaps': top10_itemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('list/', views.blog_list, name="blog_list"),
    path('top10/', views.top10_list, name='top10'),
    path('details/<title>/', views.blog_detail, name="blog_detail"),
    path('top10/details/<slug>/', views.top10_detail, name='top10_detail'),
]