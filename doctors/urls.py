from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, DepartmentViewSet, ServiceViewSet, ScheduleViewSet, DepartmentGroupViewSet

router = DefaultRouter()

router.register('doctors', DoctorViewSet)
router.register('departments', DepartmentViewSet)
router.register('department_group', DepartmentGroupViewSet)
router.register('services', ServiceViewSet)
router.register('schedules', ScheduleViewSet)

urlpatterns = [
    path('', include(router.urls))
]

