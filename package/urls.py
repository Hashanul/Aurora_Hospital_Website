from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Health_packageViewSet, Health_ServiceViewSet, HealthPackageBannerViewSet

router = DefaultRouter()

router.register(r'health_package_banner', HealthPackageBannerViewSet)
router.register(r'health_package', Health_packageViewSet)
router.register(r'health_service', Health_ServiceViewSet)

urlpatterns = [
    path('', include(router.urls))
]
