from django.shortcuts import render
from rest_framework import viewsets
from .models import Hero, HeroBadge, About, Badge, Facilities, Banner
from .serializers import HeroSerializer, HeroBadgeSerializer, AboutSerializer, BadgeSerializer, FacilitiesSerializer, BannerSerializer
from accounts.permissions import AdminPermission
# from .serializers import MenuSerializer
from .models import MenuItem,MenuContent, PopUp
from .serializers import MenuItemSerializer, MenuContentSerializer, PopUpSerializer

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


# class ContactHomeViewSet(viewsets.ModelViewSet):
#     queryset = ContactHome.objects.all()
#     serializer_class = ContactHomeSerializer
 