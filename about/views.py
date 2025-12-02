from django.shortcuts import render
from rest_framework import viewsets
from .models import BOD, ChairmanMessage, MDMessage, AboutBanner
from .serializers import BODSerializer, ChairmanMessageSerializer, MDMessageSerializer, AboutBannerSerializer
from accounts.permissions import AdminPermission


class AboutBannerViewSet(viewsets.ModelViewSet):
    queryset = AboutBanner.objects.all()
    serializer_class = AboutBannerSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class BODViewSet(viewsets.ModelViewSet):
    queryset = BOD.objects.all()
    serializer_class =  BODSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class ChairmanMessageViewSet(viewsets.ModelViewSet):
    queryset = ChairmanMessage.objects.all()
    serializer_class =  ChairmanMessageSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class MDMessageViewSet(viewsets.ModelViewSet):
    queryset = MDMessage.objects.all()
    serializer_class =  MDMessageSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)

