from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, BestDoctorViewSet, DepartmentViewSet, ServiceViewSet, ScheduleViewSet, DepartmentGroupListAPIView, DepartmentGroupRetrieveUpdateAPIView

router = DefaultRouter()

router.register('doctors', DoctorViewSet, basename='doctor')
router.register('best_doctor', BestDoctorViewSet, basename='best_doctor')
router.register('departments', DepartmentViewSet)
# router.register('department_group', DepartmentGroupViewSet)
router.register('services', ServiceViewSet)
router.register('schedules', ScheduleViewSet)
# router.register('department_group', DepartmentGroupListAPIView)
# router.register('department_group/<int:pk>', DepartmentGroupRetrieveUpdateAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('department_group/', DepartmentGroupListAPIView.as_view()),
    path('department_group/<int:pk>/', DepartmentGroupRetrieveUpdateAPIView.as_view()),
]

