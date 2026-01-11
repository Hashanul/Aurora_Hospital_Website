from django.shortcuts import render
from rest_framework import viewsets
from .models import MenuItem,MenuContent, PopUp, Hero, HeroBadge, About, Health_package, Badge, AppointmentHomeImage, HomeService
from .serializers import MenuItemSerializer, MenuContentSerializer, PopUpSerializer, HeroSerializer, HeroBadgeSerializer, AboutSerializer, Health_packageSerializer, BadgeSerializer, AppointmentHomeImageSerializer, HomeServiceSerializer
from accounts.permissions import AdminPermission
from doctors.views import CreatedByMixin



class PopUpViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = PopUp.objects.select_related('created_by').all()
    serializer_class = PopUpSerializer
    permission_classes = [AdminPermission]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().order_by('order')
    serializer_class = MenuItemSerializer


class MenuContentViewSet(viewsets.ModelViewSet):
    queryset = MenuContent.objects.select_related('menu').all()
    serializer_class = MenuContentSerializer

 
class HeroViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = Hero.objects.select_related('created_by').all()
    serializer_class = HeroSerializer
    permission_classes = [AdminPermission]


class HeroBadgeViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = HeroBadge.objects.select_related('created_by').all()
    serializer_class = HeroBadgeSerializer
    permission_classes = [AdminPermission]



class AboutViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = About.objects.select_related('created_by').all()
    serializer_class = AboutSerializer
    permission_classes = [AdminPermission]


class Health_packageViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = Health_package.objects.select_related('created_by').all()
    serializer_class = Health_packageSerializer
    permission_classes = [AdminPermission]



class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = [AdminPermission]


# class FacilitiesViewSet(CreatedByMixin, viewsets.ModelViewSet):
#     queryset = Facilities.objects.select_related('created_by').all()
#     serializer_class = FacilitiesSerializer
#     permission_classes = [AdminPermission]


class AppointmentHomeImageViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = AppointmentHomeImage.objects.select_related('created_by').all()
    serializer_class = AppointmentHomeImageSerializer
    permission_classes = [AdminPermission]
 

 
class HomeServiceViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = HomeService.objects.select_related('created_by').all()
    serializer_class = HomeServiceSerializer
    permission_classes = [AdminPermission]

