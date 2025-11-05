from django.shortcuts import render
from rest_framework import viewsets
from .models import Hero, Banner
from .serializers import HeroSerializer, BannerSerializer


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    

