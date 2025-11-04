from django.shortcuts import render
from rest_framework import viewsets
from .models import NewsCategories, News
from .serializers import NewsCategoriesSerializer, NewsSerializer

class NewsCategoryViewSet(viewsets.ModelViewSet):
    queryset = NewsCategories.objects.all()
    serializer_class = NewsCategoriesSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer