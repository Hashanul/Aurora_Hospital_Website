from django.shortcuts import render
from rest_framework import viewsets
from .models import RoomRent, Equipment, FeedbackBanner, Feedback
from .serializers import RoomRentSerializer, EquipmentSerializer, FeedbackBannerSerializer, FeedbackSerializer
from accounts.permissions import AdminPermission


class RoomRentViewSet(viewsets.ModelViewSet):
    queryset = RoomRent.objects.all()
    serializer_class = RoomRentSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)

class FeedbackBannerViewSet(viewsets.ModelViewSet):
    queryset = FeedbackBanner.objects.all()
    serializer_class = FeedbackBannerSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)
    

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)
