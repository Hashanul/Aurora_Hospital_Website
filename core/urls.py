
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# Import all ViewSets from apps
from home.views import HeroViewSet, BannerViewSet, ContactViewSet
from doctors.views import DoctorViewSet, DepartmentViewSet, ServiceViewSet, ScheduleViewSet, DepartmentGroupViewSet
from patients.views import PatientViewSet
from news.views import NewsCategoryViewSet, NewsViewSet
from appointment.views import AppointmentViewSet
from package.views import Health_packageViewSet
# from accounts.views import RegisterViewSet, UserViewSet



# Create a single central router for all API endpoints
router = DefaultRouter()

# Home app
router.register('hero', HeroViewSet)
router.register('banners', BannerViewSet)
router.register('contacts', ContactViewSet)

# Doctors app
router.register('doctors', DoctorViewSet)
router.register('departments', DepartmentViewSet)
router.register('department_group', DepartmentGroupViewSet)
router.register('services', ServiceViewSet)
router.register('schedules', ScheduleViewSet)

# Patients app
router.register('patients', PatientViewSet)

# News app
router.register('news_categories', NewsCategoryViewSet)
router.register('news', NewsViewSet)

# Appointment app
router.register('appointments', AppointmentViewSet)

# Package app
router.register('health_package', Health_packageViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
#     path('api/', include('home.urls')),
#     path('api/', include('doctors.urls')),
#     path('api/', include('patients.urls')),
#     path('api/', include('news.urls')),


    path('api/', include(router.urls)),
    path('api/', include('accounts.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 




