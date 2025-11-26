from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeroViewSet, HeroBadgeViewSet, AboutViewSet, BadgeViewSet, FacilitiesViewSet, BannerViewSet, ContactHomeViewSet

router = DefaultRouter()

router.register('hero', HeroViewSet)
router.register('hero_badge', HeroBadgeViewSet)
router.register('about', AboutViewSet)
router.register('badge', BadgeViewSet)
router.register('banners', BannerViewSet)
router.register('contacts', ContactHomeViewSet)
router.register('facilities', FacilitiesViewSet)


urlpatterns = [
    path('', include(router.urls))
]

