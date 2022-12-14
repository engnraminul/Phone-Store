from django import views
from django.contrib import admin
from django.urls import path, include
from StoreMain import views 
from django.conf import settings
from django.conf.urls.static import static
from .views import robots_txt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Phone.urls')),
    path('page/', include('page.urls')),
    path('blog/', include('blog.urls')),
    path('tinymce/', include('tinymce.urls')),
    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#admin pannel header and title customization
admin.site.site_header = "SpecBuzz"
admin.site.site_title = "SpecBuzz"
admin.site.index_title = "SpecBuzz Index"