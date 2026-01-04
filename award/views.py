from django.shortcuts import render
from rest_framework import viewsets
from .models import Award, AwardBanner
from .serializers import AwardSerializer, AwardBannerSerializer
from accounts.permissions import AdminPermission
from doctors.views import CreatedByMixin


class AwardBannerViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = AwardBanner.objects.select_related('created_by').all().order_by('-created_at')
    serializer_class = AwardBannerSerializer
    permission_classes = [AdminPermission]

  

class AwardViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = Award.objects.select_related('created_by').all().order_by('-created_at')
    serializer_class = AwardSerializer
    permission_classes = [AdminPermission]



