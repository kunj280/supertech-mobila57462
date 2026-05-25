from django.urls import include,path
from django.conf.urls.static import static
from django.conf import settings
   
    
  #Url Set
  
urlpatterns = [
    path('adminapp/', include('adminapp.urls')),
    path('', include('userapp.urls')),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)