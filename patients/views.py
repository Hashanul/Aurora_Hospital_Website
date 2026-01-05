from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient, PatientBanner
from .serializers import PatientSerializer, PatientBannerSerializer
from accounts.permissions import AdminPermission
from doctors.views import CreatedByMixin


class PatientBannerViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = PatientBanner.objects.select_related('created_by').all()
    serializer_class = PatientBannerSerializer
    permission_classes = [AdminPermission]


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    
