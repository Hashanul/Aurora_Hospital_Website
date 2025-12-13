from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Health_Check_upBannerViewSet, Health_Check_upViewSet, RoomRentViewSet,EquipmentBannerViewSet, VisitorPackageBannerViewSet, EquipmentViewSet, RoomRentBannerViewSet, FeedbackBannerViewSet, FeedbackViewSet, VisitorPackageViewSet, PackageDetailViewSet, ServiceBannerViewSet, VisitorServiceViewSet, FacilitiesBannerViewSet

router = DefaultRouter()

router.register(r'health_package_banner', Health_Check_upBannerViewSet)
router.register(r'health_package', Health_Check_upViewSet)
router.register(r'service_banner', ServiceBannerViewSet)
router.register(r'visitor_service', VisitorServiceViewSet)
router.register(r'facilities_banner', FacilitiesBannerViewSet)
router.register(r'visitor_package_banner', VisitorPackageBannerViewSet)
router.register(r'visitor_package', VisitorPackageViewSet)
router.register(r'package_detail', PackageDetailViewSet)
router.register(r'room_rent_banner', RoomRentBannerViewSet)
router.register(r'room_rent', RoomRentViewSet)
router.register(r'equipment_banner', EquipmentBannerViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'feedback_banner', FeedbackBannerViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls))
]
