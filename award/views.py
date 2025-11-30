from django.shortcuts import render
from rest_framework import viewsets
from .models import Award, AwardBanner
from .serializers import AwardSerializer, AwardBannerSerializer
from accounts.permissions import AdminPermission


class AwardBannerViewSet(viewsets.ModelViewSet):
    queryset = AwardBanner.objects.all().order_by('-created_at')
    serializer_class = AwardBannerSerializer
    permission_classes = [AdminPermission]


    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)
            

class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all().order_by('-created_at')
    serializer_class = AwardSerializer
    permission_classes = [AdminPermission]


    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)

