from django.shortcuts import render
from rest_framework import viewsets
from .models import NewsCategories, News
from .serializers import NewsCategoriesSerializer, NewsSerializer
from accounts.permissions import NewsPermission

class NewsCategoryViewSet(viewsets.ModelViewSet):
    queryset = NewsCategories.objects.all()
    serializer_class = NewsCategoriesSerializer
    permission_classes = [NewsPermission]

    
    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [NewsPermission]

    
    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)
