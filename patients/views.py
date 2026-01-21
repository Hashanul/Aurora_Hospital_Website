from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient, PatientBanner, PatientStory, PatientStoryBanner
from .serializers import PatientSerializer, PatientBannerSerializer, PatientStoryBannerSerializer, PatientStorySerializer
from accounts.permissions import AdminPermission
from django_filters.rest_framework import DjangoFilterBackend
from doctors.views import CreatedByMixin
from .filters import PatientStoryFilter


class PatientBannerViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = PatientBanner.objects.select_related('created_by')
    serializer_class = PatientBannerSerializer
    permission_classes = [AdminPermission]


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientStoryBannerViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = PatientStoryBanner.objects.select_related('created_by')
    serializer_class = PatientStoryBannerSerializer
    permission_classes = [AdminPermission]


class PatientStoryViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = PatientStory.objects.select_related('doctor', 'department', 'created_by').all()
    serializer_class = PatientStorySerializer
    permission_classes = [AdminPermission]

    filter_backends = [DjangoFilterBackend]
    filterset_class = PatientStoryFilter
    ordering = ['order']

    
