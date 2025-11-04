from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor, Department
from .serializers import DoctorSerializer, DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

