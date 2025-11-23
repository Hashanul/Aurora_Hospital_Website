from rest_framework import viewsets
from .models import Role
from .serializers import RoleSerializer
from .permissions import RolePermission


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [RolePermission]  # Restrict access

# permissions/views.py
from rest_framework import viewsets
from django.contrib.auth.models import Permission

from .serializers import PermissionSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

# permissions/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import (
    UserPermissionAssignSerializer,
    PermissionSerializer
)

class UserPermissionViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def assign(self, request):
        """
        POST /user-permissions/assign/
        """
        serializer = UserPermissionAssignSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "status": "success",
            "user": user.username,
            "assigned_permissions": list(user.get_user_permissions())
        })

    @action(detail=True, methods=['get'])
    def list_permissions(self, request, pk=None):
        """
        GET /user-permissions/<pk>/list_permissions/
        """
        user = User.objects.get(id=pk)
        permissions = user.user_permissions.all()
        ser = PermissionSerializer(permissions, many=True)

        return Response(ser.data)
