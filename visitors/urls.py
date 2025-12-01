from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomRentViewSet, EquipmentViewSet, FeedbackBannerViewSet, FeedbackViewSet, VisitorPackageViewSet, PackageDetailViewSet

router = DefaultRouter()

router.register(r'visitor_package', VisitorPackageViewSet)
router.register(r'package_detail', PackageDetailViewSet)
router.register(r'room_rent', RoomRentViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'feedback_banner', FeedbackBannerViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls))
]
