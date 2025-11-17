from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeroViewSet, BadgeViewSet, FacilitiesViewSet, BannerViewSet, ContactViewSet

router = DefaultRouter()

router.register('hero', HeroViewSet)
router.register('badge', BadgeViewSet)
router.register('banners', BannerViewSet)
router.register('contacts', ContactViewSet)
router.register('facilities', FacilitiesViewSet)


urlpatterns = [
    path('', include(router.urls))
]

