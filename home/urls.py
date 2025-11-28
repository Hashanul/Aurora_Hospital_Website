from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeroViewSet, HeroBadgeViewSet, AboutViewSet, BadgeViewSet, FacilitiesViewSet, BannerViewSet, ContactHomeViewSet, MenuItemViewSet, MenuContentViewSet

router = DefaultRouter()

router.register("navbar", MenuItemViewSet, basename="navbar")
router.register("contents", MenuContentViewSet, basename="contents")
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



