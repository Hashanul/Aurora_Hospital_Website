from django.shortcuts import render
from rest_framework import viewsets
from .models import Health_package
from .serializers import Health_packageSerializer


class Health_packageViewSet(viewsets.ModelViewSet):
    queryset = Health_package.objects.all()
    serializer_class = Health_packageSerializer

