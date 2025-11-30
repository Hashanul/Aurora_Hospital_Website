from rest_framework.routers import DefaultRouter
from .views import AwardViewSet, AwardBannerViewSet

router = DefaultRouter()
router.register(r'award_banners', AwardBannerViewSet, basename='award_banners')
router.register(r'awards', AwardViewSet, basename='awards')

urlpatterns = router.urls
