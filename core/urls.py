
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('home.urls')),
    path('api/', include('doctors.urls')),
    path('api/', include('patients.urls')),
    path('api/', include('news.urls')),
    path('api/', include('appointment.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 