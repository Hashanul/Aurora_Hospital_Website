from django.shortcuts import render
from rest_framework import viewsets
from .models import Health_package, Health_Service
from .serializers import Health_packageSerializer, Health_ServiceSerializer
from accounts.permissions import AdminPermission


class Health_packageViewSet(viewsets.ModelViewSet):
    queryset = Health_package.objects.all()
    serializer_class = Health_packageSerializer
    permission_classes = [AdminPermission]


    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)

class Health_ServiceViewSet(viewsets.ModelViewSet):
    queryset = Health_Service.objects.all()
    serializer_class = Health_ServiceSerializer
    permission_classes = [AdminPermission]

