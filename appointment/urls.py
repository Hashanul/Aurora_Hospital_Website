from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, AppointmentBannerViewSet

router = DefaultRouter()

router.register('appointment_banner', AppointmentBannerViewSet)
router.register('appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]

