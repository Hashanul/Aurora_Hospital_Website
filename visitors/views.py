from django.shortcuts import render
from rest_framework import viewsets
from .models import RoomRent, FeedbackBanner, Feedback
from .serializers import RoomRentSerializer, FeedbackBannerSerializer, FeedbackSerializer



class RoomRentViewSet(viewsets.ModelViewSet):
    queryset = RoomRent.objects.all()
    serializer_class = RoomRentSerializer


class FeedbackBannerViewSet(viewsets.ModelViewSet):
    queryset = FeedbackBanner.objects.all()
    serializer_class = FeedbackBannerSerializer
    

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
