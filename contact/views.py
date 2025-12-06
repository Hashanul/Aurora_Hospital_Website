from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import ContactPage, ContactUs, Contact_data, ContactBanner
from .serializers import ContactPageSerializer, ContactUsSerializer, Contact_dataSerializer, ContactBannerSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView



class ContactBannerViewSet(viewsets.ModelViewSet):
    queryset = ContactBanner.objects.all()
    serializer_class = ContactBannerSerializer
  
    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class ContactPageViewSet(viewsets.ModelViewSet):
    queryset = ContactPage.objects.all()
    serializer_class = ContactPageSerializer

  
    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


    # def perform_create(self, serializer):
    #     user = self.request.user

    #     if user.is_authenticated:
    #         serializer.save(created_by=user)
    #     else:
    #         serializer.save(created_by=None)

class Contact_dataListAPIView(ListAPIView):
    queryset = Contact_data.objects.all()
    serializer_class = Contact_dataSerializer


class Contact_dataRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Contact_data.objects.all()
    serializer_class = Contact_dataSerializer

