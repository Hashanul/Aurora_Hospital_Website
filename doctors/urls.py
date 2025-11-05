from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, DepartmentViewSet, ServiceViewSet, ScheduleViewSet, DepartmentGroupViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'department_group', DepartmentGroupViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'schedules', ScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
