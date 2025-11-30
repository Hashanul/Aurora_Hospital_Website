from django.shortcuts import render
from rest_framework import viewsets
from .models import NewsCategories, News, NewsBanner
from .serializers import NewsCategoriesSerializer, NewsSerializer, NewsBannerSerializer
from accounts.permissions import AdminPermission

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter



class NewsBannerViewSet(viewsets.ModelViewSet):
    queryset = NewsBanner.objects.all()
    serializer_class = NewsBannerSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)
            
class NewsCategoryViewSet(viewsets.ModelViewSet):
    queryset = NewsCategories.objects.all()
    serializer_class = NewsCategoriesSerializer
    permission_classes = [AdminPermission]

    
    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AdminPermission]

    filter_backends = [DjangoFilterBackend, SearchFilter]

    # Filter by related model field
    filterset_fields = {
        'category__name': ['exact', 'icontains'], 
    }

    # Search in title, richtext
    search_fields = ['title', 'richtext', 'category__name']

    
    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)

