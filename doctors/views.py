from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Doctor, BestDoctor, Department, ChamberTime, DepartmentGroup, DepartmentBanner, DoctorBanner
from .serializers import DoctorSerializer, BestDoctorSerializer, DepartmentSerializer, ChamberTimeSerializer, DepartmentGroupSerializer, DepartmentBannerSerializer, DoctorBannerSerializer
from accounts.permissions import AdminPermission
from .filters import ChamberTimeFilter
from .pagination import DoctorPagination


class DoctorBannerViewSet(viewsets.ModelViewSet):
    queryset = DoctorBanner.objects.all()
    serializer_class = DoctorBannerSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class DepartmentBannerViewSet(viewsets.ModelViewSet):
    queryset = DepartmentBanner.objects.all()
    serializer_class = DepartmentBannerSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [AdminPermission]

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination
        
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department__name']

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)

    def get_queryset(self):
        queryset = super().get_queryset()

        department_name = self.request.query_params.get('department_name')
        if department_name:
            queryset = queryset.filter(department__slug=department_name)

        department_id = self.request.query_params.get('department_id')
        if department_id:
            queryset = queryset.filter(department_id=department_id)


        doctor_name = self.request.query_params.get('doctor_name')
        if doctor_name:
            queryset = queryset.filter(drName__icontains=doctor_name)

        return queryset


class ChamberTimeViewSet(viewsets.ModelViewSet):
    queryset = ChamberTime.objects.all()
    serializer_class = ChamberTimeSerializer
    permission_classes = [AdminPermission]

    filter_backends = [DjangoFilterBackend]
    filterset_class = ChamberTimeFilter

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class BestDoctorViewSet(viewsets.ModelViewSet):
    queryset = BestDoctor.objects.all()
    serializer_class = BestDoctorSerializer

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class DepartmentGroupViewSet(viewsets.ModelViewSet):
    queryset = DepartmentGroup.objects.all()
    serializer_class = DepartmentGroupSerializer
    permission_classes = [AdminPermission]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['group_name']   # 👈 THIS ENABLES ?group_name=
    search_fields = ['group_name']

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


# class DepartmentGroupListAPIView(ListAPIView):
#     queryset = DepartmentGroup.objects.all()
#     serializer_class = DepartmentGroupSerializer
#     permission_classes = [AdminPermission]


# class DepartmentGroupRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = DepartmentGroup.objects.all()
#     serializer_class = DepartmentGroupSerializer
#     permission_classes = [AdminPermission]
 