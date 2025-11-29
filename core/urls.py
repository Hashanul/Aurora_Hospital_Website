
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from home.urls import router as supporter_router
from doctors.urls import router as supporter_router_doctor
from patients.urls import router as supporter_router_patients
from news.urls import router as supporter_router_news
from appointment.urls import router as supporter_router_appointment
from package.urls import router as supporter_router_package
from accounts.urls import router as supporter_router_accounts
from award.urls import router as supporter_router_award
from contact.urls import router as supporter_router_contact
from about.urls import router as supporter_router_about


# Create a single central router for all API endpoints
router = DefaultRouter()
router.registry.extend(supporter_router.registry)
router.registry.extend(supporter_router_doctor.registry)
router.registry.extend(supporter_router_patients.registry)
router.registry.extend(supporter_router_news.registry)
router.registry.extend(supporter_router_appointment.registry)
router.registry.extend(supporter_router_package.registry)
router.registry.extend(supporter_router_accounts.registry)
router.registry.extend(supporter_router_award.registry)
router.registry.extend(supporter_router_contact.registry)
router.registry.extend(supporter_router_about.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('accounts.urls')),
    path('api/', include('news.urls')),
    path('api/', include('doctors.urls')),

    # CKEditor upload endpoints (make available at project root)
    path('ckeditor5/', include('django_ckeditor_5.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 



