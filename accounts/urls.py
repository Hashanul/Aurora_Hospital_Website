from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoleViewSet


router = DefaultRouter()
router.register('role', RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),   # JWT endpoints
]






