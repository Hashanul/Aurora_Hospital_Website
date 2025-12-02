from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, BestDoctorViewSet, DepartmentViewSet, HomeServiceViewSet, ChamberTimeViewSet, DepartmentGroupViewSet, DepartmentBannerViewSet, DoctorBannerViewSet

router = DefaultRouter()

router.register('department_banner', DepartmentBannerViewSet)
router.register('doctor_banner', DoctorBannerViewSet)
router.register('doctors', DoctorViewSet, basename='doctor')
router.register('best_doctor', BestDoctorViewSet, basename='best_doctor')
router.register('departments', DepartmentViewSet)
router.register('department_group', DepartmentGroupViewSet)
router.register('home_services', HomeServiceViewSet, basename='home_service')
router.register('chamber_time', ChamberTimeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('department_group/', DepartmentGroupListAPIView.as_view()),
    # path('department_group/<int:pk>/', DepartmentGroupRetrieveUpdateAPIView.as_view()),
]

