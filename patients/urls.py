from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PatientBannerViewSet

router = DefaultRouter()

router.register(r'patient_banner', PatientBannerViewSet)
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]