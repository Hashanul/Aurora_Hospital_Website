from rest_framework import viewsets
from .models import Role
from .serializers import RoleSerializer
from .permissions import RolePermission


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [RolePermission]  # Restrict access

