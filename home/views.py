from django.shortcuts import render
from rest_framework import viewsets
from .models import Hero, HeroBadge, About_us, Badge, Facilities, Banner, Contact
from .serializers import HeroSerializer, HeroBadgeSerializer, AboutSerializer, BadgeSerializer, FacilitiesSerializer, BannerSerializer, ContactSerializer
from accounts.permissions import AdminPermission


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class HeroBadgeViewSet(viewsets.ModelViewSet):
    queryset = HeroBadge.objects.all()
    serializer_class = HeroBadgeSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About_us.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)
            

class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)



class FacilitiesViewSet(viewsets.ModelViewSet):
    queryset = Facilities.objects.all()
    serializer_class = FacilitiesSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [AdminPermission]
    
    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
 