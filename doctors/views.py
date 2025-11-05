from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor, Department, Service, Schedule, DepartmentGroup
from .serializers import DoctorSerializer, DepartmentSerializer, ServiceSerializer, ScheduleSerializer, DepartmentGroupSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class DepartmentGroupViewSet(viewsets.ModelViewSet):
    queryset = DepartmentGroup.objects.all()
    serializer_class = DepartmentGroupSerializer

    