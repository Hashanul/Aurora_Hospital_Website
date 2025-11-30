from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomRentViewSet, FeedbackBannerViewSet, FeedbackViewSet

router = DefaultRouter()

router.register(r'room_rent', RoomRentViewSet)
router.register(r'feedback_banner', FeedbackBannerViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls))
]
