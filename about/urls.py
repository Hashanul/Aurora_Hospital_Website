from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BODViewSet, ChairmanMessageViewSet, MDMessageViewSet, AboutBannerViewSet

router = DefaultRouter()

router.register(r'bod', BODViewSet)
router.register(r'chairman_message', ChairmanMessageViewSet)
router.register(r'md_message', MDMessageViewSet)
router.register(r'about_banner', AboutBannerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

