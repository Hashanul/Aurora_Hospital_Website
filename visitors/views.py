from django.shortcuts import render
from rest_framework import viewsets
from .models import VisitorPackage, RoomRentBanner, VisitorPackageBanner, PackageDetail, FacilitiesBanner, RoomRent, EquipmentBanner, Equipment, FeedbackBanner, Feedback, ServiceBanner, VisitorService
from .serializers import VisitorPackageSerializer, VisitorPackageBannerSerializer, RoomRentBannerSerializer,  PackageDetailSerializer, RoomRentSerializer, EquipmentBannerSerializer, EquipmentSerializer, FeedbackBannerSerializer, FeedbackSerializer, ServiceBannerSerializer, VisitorServiceSerializer, FacilitiesBannerSerializer
from accounts.permissions import AdminPermission
from django_filters.rest_framework import DjangoFilterBackend


class ServiceBannerViewSet(viewsets.ModelViewSet):
    queryset = ServiceBanner.objects.all()
    serializer_class = ServiceBannerSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)



class VisitorServiceViewSet(viewsets.ModelViewSet):
    queryset = VisitorService.objects.all()
    serializer_class = VisitorServiceSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class FacilitiesBannerViewSet(viewsets.ModelViewSet):
    queryset = FacilitiesBanner.objects.all()
    serializer_class = FacilitiesBannerSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class VisitorPackageBannerViewSet(viewsets.ModelViewSet):
    queryset = VisitorPackageBanner.objects.all()
    serializer_class = VisitorPackageBannerSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class VisitorPackageViewSet(viewsets.ModelViewSet):
    queryset = VisitorPackage.objects.all()
    serializer_class = VisitorPackageSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by = user)
        else:
            serializer.save(created_by=None)


class PackageDetailViewSet(viewsets.ModelViewSet):
    queryset = PackageDetail.objects.all()
    serializer_class = PackageDetailSerializer
    permission_classes = [AdminPermission]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['package_title']

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by = user)
        else:
            serializer.save(created_by=None)

class RoomRentBannerViewSet(viewsets.ModelViewSet):
    queryset = RoomRentBanner.objects.all()
    serializer_class = RoomRentBannerSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


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

class EquipmentBannerViewSet(viewsets.ModelViewSet):
    queryset = EquipmentBanner.objects.all()
    serializer_class = EquipmentBannerSerializer
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


    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)
