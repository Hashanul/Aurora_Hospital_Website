from django.shortcuts import render
from rest_framework import viewsets
from .models import NewsCategories, News, NewsBanner
from .serializers import NewsCategoriesSerializer, NewsSerializer, NewsBannerSerializer
from accounts.permissions import AdminPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from doctors.views import CreatedByMixin


class NewsBannerViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = NewsBanner.objects.select_related('created_by').all()
    serializer_class = NewsBannerSerializer
    permission_classes = [AdminPermission]

            
class NewsCategoryViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = NewsCategories.objects.select_related('created_by').all()
    serializer_class = NewsCategoriesSerializer
    permission_classes = [AdminPermission]



class NewsViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = News.objects.select_related('category', 'created_by').all()
    serializer_class = NewsSerializer
    permission_classes = [AdminPermission]

    filter_backends = [DjangoFilterBackend, SearchFilter]

    # Filter by related model field
    filterset_fields = {
        'category__name': ['exact', 'icontains'], 
    }

    # Search in title, richtext
    search_fields = ['title', 'richtext', 'category__name']

    

