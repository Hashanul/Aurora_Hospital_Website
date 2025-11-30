from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, BestDoctorViewSet, DepartmentViewSet, ServiceViewSet, ChamberTimeViewSet, DepartmentGroupListAPIView, DepartmentGroupRetrieveUpdateAPIView, DepartmentBannerViewSet, DoctorBannerViewSet

router = DefaultRouter()

router.register('department_banner', DepartmentBannerViewSet)
router.register('doctor_banner', DoctorBannerViewSet)
router.register('doctors', DoctorViewSet, basename='doctor')
router.register('best_doctor', BestDoctorViewSet, basename='best_doctor')
router.register('departments', DepartmentViewSet)
# router.register('department_group', DepartmentGroupViewSet)
router.register('services', ServiceViewSet)
router.register('chamber_time', ChamberTimeViewSet)
# router.register('department_group', DepartmentGroupListAPIView)
# router.register('department_group/<int:pk>', DepartmentGroupRetrieveUpdateAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('department_group/', DepartmentGroupListAPIView.as_view()),
    path('department_group/<int:pk>/', DepartmentGroupRetrieveUpdateAPIView.as_view()),
]

