from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, AppointmentBannerViewSet, ReportViewSet, ReportPortalViewset, AppointmentPackageBannerViewSet, AppointmentPackageViewSet, AppointmentPackageHeaderViewSet

router = DefaultRouter()

router.register('appointment_banner', AppointmentBannerViewSet)
router.register('appointments', AppointmentViewSet)
router.register('appointment_package_banner', AppointmentPackageBannerViewSet)
router.register('appointment_package_header', AppointmentPackageHeaderViewSet)
router.register('appointment_package', AppointmentPackageViewSet)
router.register('report', ReportViewSet)
router.register('report_portal', ReportPortalViewset)

urlpatterns = [
    path('', include(router.urls))
]

