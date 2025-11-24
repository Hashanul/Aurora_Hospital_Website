from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsCategoryViewSet, NewsViewSet

router = DefaultRouter()

router.register(r'news_categories', NewsCategoryViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]


