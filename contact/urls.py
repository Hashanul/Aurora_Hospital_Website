from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactPageViewSet, ContactUsViewSet, Contact_dataViewSet, ContactBannerViewSet

router = DefaultRouter()

router.register('contact_banner', ContactBannerViewSet)
router.register('contact_page', ContactPageViewSet)
router.register('contact_us', ContactUsViewSet)
router.register('contact_data', Contact_dataViewSet)

urlpatterns = [
    path('', include(router.urls))
]