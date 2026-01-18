from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PatientBannerViewSet, PatientStoryViewSet, PatientStoryBannerViewSet

router = DefaultRouter()

router.register(r'patient_banner', PatientBannerViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'patient_storie_banner', PatientStoryBannerViewSet)
router.register(r'patient_stories', PatientStoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]