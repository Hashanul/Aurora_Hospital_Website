from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Health_packageViewSet

router = DefaultRouter()

router.register(r'health_package', Health_packageViewSet)

urlpatterns = [
    path('', include(router.urls))
]
