from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, AppointmentBannerViewSet, ReportViewSet

router = DefaultRouter()

router.register('appointment_banner', AppointmentBannerViewSet)
router.register('appointments', AppointmentViewSet)
router.register('report', ReportViewSet)

urlpatterns = [
    path('', include(router.urls))
]

