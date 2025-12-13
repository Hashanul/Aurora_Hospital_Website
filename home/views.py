from django.shortcuts import render
from rest_framework import viewsets
from .models import MenuItem,MenuContent, PopUp, Hero, HeroBadge, About, Health_package, Badge, Facilities, AppointmentHomeImage, HomeService
from .serializers import MenuItemSerializer, MenuContentSerializer, PopUpSerializer, HeroSerializer, HeroBadgeSerializer, AboutSerializer, Health_packageSerializer, BadgeSerializer, FacilitiesSerializer, AppointmentHomeImageSerializer, HomeServiceSerializer
from accounts.permissions import AdminPermission



class PopUpViewSet(viewsets.ModelViewSet):
    queryset = PopUp.objects.all()
    serializer_class = PopUpSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuContentViewSet(viewsets.ModelViewSet):
    queryset = MenuContent.objects.all()
    serializer_class = MenuContentSerializer

 
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
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class Health_packageViewSet(viewsets.ModelViewSet):
    queryset = Health_package.objects.all()
    serializer_class = Health_packageSerializer
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

class AppointmentHomeImageViewSet(viewsets.ModelViewSet):
    queryset = AppointmentHomeImage.objects.all()
    serializer_class = AppointmentHomeImageSerializer
    permission_classes = [AdminPermission]
    
    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


# class ContactHomeViewSet(viewsets.ModelViewSet):
#     queryset = ContactHome.objects.all()
#     serializer_class = ContactHomeSerializer
 



 
class HomeServiceViewSet(viewsets.ModelViewSet):
    queryset = HomeService.objects.all()
    serializer_class = HomeServiceSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)
