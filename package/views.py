from django.shortcuts import render
from rest_framework import viewsets
from .models import Health_package
from .serializers import Health_packageSerializer


class Health_packageViewSet(viewsets.ModelViewSet):
    queryset = Health_package.objects.all()
    serializer_class = Health_packageSerializer

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)

