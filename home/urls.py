from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeroViewSet, BannerViewSet, ContactViewSet

router = DefaultRouter()

router.register('hero', HeroViewSet)
router.register('banners', BannerViewSet)
router.register('contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls))
]

