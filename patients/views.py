from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient, PatientBanner
from .serializers import PatientSerializer, PatientBannerSerializer
from accounts.permissions import AdminPermission


class PatientBannerViewSet(viewsets.ModelViewSet):
    queryset = PatientBanner.objects.all()
    serializer_class = PatientBannerSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    
