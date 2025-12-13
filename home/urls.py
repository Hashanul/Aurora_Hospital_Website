from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, MenuContentViewSet, PopUpViewSet, HeroViewSet, HeroBadgeViewSet, AboutViewSet, Health_packageViewSet, BadgeViewSet, FacilitiesViewSet, AppointmentHomeImageViewSet, HomeServiceViewSet

router = DefaultRouter()

router.register("popup", PopUpViewSet)
router.register("navbar", MenuItemViewSet, basename="navbar")
router.register("contents", MenuContentViewSet, basename="contents")
router.register('hero', HeroViewSet)
router.register('hero_badge', HeroBadgeViewSet)
router.register('about', AboutViewSet)
router.register(r'health_package', Health_packageViewSet)
router.register('badge', BadgeViewSet)
router.register('appointment_home_image', AppointmentHomeImageViewSet)
router.register('facilities', FacilitiesViewSet)
router.register('home_services', HomeServiceViewSet, basename='home_service')



urlpatterns = [
    path('', include(router.urls))
]



