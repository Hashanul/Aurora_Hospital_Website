from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactPageViewSet, ContactUsViewSet

router = DefaultRouter()

router.register('contact_page', ContactPageViewSet)
router.register('contact_us', ContactUsViewSet)

urlpatterns = [
    path('', include(router.urls))
]