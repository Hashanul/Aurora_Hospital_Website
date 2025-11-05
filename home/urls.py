from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeroViewSet, BannerViewSet

router = DefaultRouter()

router.register('hero', HeroViewSet)
router.register('banners', BannerViewSet)

urlpatterns = [
    path('', include(router.urls))
]

