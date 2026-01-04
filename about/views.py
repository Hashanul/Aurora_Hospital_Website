from django.shortcuts import render
from rest_framework import viewsets
from .models import BOD, ChairmanMessage, MDMessage, AboutBanner
from .serializers import BODSerializer, ChairmanMessageSerializer, MDMessageSerializer, AboutBannerSerializer
from accounts.permissions import AdminPermission
from doctors.views import CreatedByMixin


class AboutBannerViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = AboutBanner.objects.select_related('created_by') .all()
    serializer_class = AboutBannerSerializer
    permission_classes = [AdminPermission]


class BODViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = BOD.objects.select_related('bod_drName', 'created_by') .all()
    serializer_class =  BODSerializer
    permission_classes = [AdminPermission]



class ChairmanMessageViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = ChairmanMessage.objects.select_related('created_by') .all()
    serializer_class =  ChairmanMessageSerializer
    permission_classes = [AdminPermission]


class MDMessageViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = MDMessage.objects.select_related('created_by') .all()
    serializer_class =  MDMessageSerializer
    permission_classes = [AdminPermission]



