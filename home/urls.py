from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MenuItemViewSet,
    MenuContentViewSet,
    PopUpViewSet,
    HeroViewSet,
    HeroBadgeViewSet,
    AboutViewSet,
    Health_packageViewSet,
    BadgeViewSet,
    AppointmentHomeImageViewSet,
    HomeServiceViewSet,
    CorporateServiceViewSet,
    CorporateCarouselViewSet,
)

router = DefaultRouter()

router.register("popup", PopUpViewSet)
router.register("navbar", MenuItemViewSet, basename="navbar")
router.register("contents", MenuContentViewSet, basename="contents")
router.register("hero", HeroViewSet)
router.register("hero_badge", HeroBadgeViewSet)
router.register("about", AboutViewSet)
router.register("health_package", Health_packageViewSet)
router.register("badge", BadgeViewSet)
router.register("appointment_home_image", AppointmentHomeImageViewSet)
router.register("home_services", HomeServiceViewSet, basename="home_service")
router.register("corporate_service", CorporateServiceViewSet)
router.register(
    "corporate_carousel", CorporateCarouselViewSet, basename="corporate_carousel"
)

urlpatterns = [path("", include(router.urls))]
