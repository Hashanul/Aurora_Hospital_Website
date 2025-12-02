from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoleViewSet
from .views import PermissionViewSet, UserPermissionViewSet


router = DefaultRouter()
router.register('role', RoleViewSet)
router.register("user-permissions", UserPermissionViewSet, basename="user-permissions")
router.register("permissions", PermissionViewSet, basename="permissions")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),   # JWT endpoints
]






