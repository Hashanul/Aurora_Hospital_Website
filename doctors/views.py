from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Doctor, BestDoctor, Department, ChamberTime, DepartmentGroup, DepartmentBanner, DoctorBanner
from .serializers import DoctorSerializer, BestDoctorSerializer, DepartmentSerializer, ChamberTimeSerializer, DepartmentGroupSerializer, DepartmentBannerSerializer, DoctorBannerSerializer
from accounts.permissions import AdminPermission
from .filters import ChamberTimeFilter
from .pagination import DoctorPagination


class CreatedByMixin:
    def perform_create(self, serializer):
        user = self.request.user

        if user.is_authenticated:
            serializer.save(created_by=user)
        else:
            serializer.save(created_by=None)


class DoctorBannerViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = DoctorBanner.objects.select_related('created_by')
    serializer_class = DoctorBannerSerializer
    permission_classes = [AdminPermission]


class DepartmentBannerViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = DepartmentBanner.objects.select_related('created_by')
    serializer_class = DepartmentBannerSerializer
    permission_classes = [AdminPermission]



class DepartmentViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = Department.objects.select_related('created_by')
    serializer_class = DepartmentSerializer
    permission_classes = [AdminPermission]



class DoctorViewSet(CreatedByMixin, viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination
        
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['department__name']


    def get_queryset(self):
        """
        Optimized queryset:
        - select_related for FK fields
        - supports multiple query params
        """

        queryset = (
            Doctor.objects
            .select_related('department', 'created_by')
            .all()
        )

        # 🔹 filter by department slug
        department_name = self.request.query_params.get('department_name')
        if department_name:
            queryset = queryset.filter(department__slug=department_name)

        # 🔹 filter by department id
        department_id = self.request.query_params.get('department_id')
        if department_id:
            queryset = queryset.filter(department_id=department_id)

        # 🔹 search by doctor name
        doctor_name = self.request.query_params.get('doctor_name')
        if doctor_name:
            queryset = queryset.filter(drName__icontains=doctor_name)

        return queryset


class ChamberTimeViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = (
        ChamberTime.objects
        .select_related('drCode', 'created_by')
    )
    serializer_class = ChamberTimeSerializer
    permission_classes = [AdminPermission]

    filter_backends = [DjangoFilterBackend]
    filterset_class = ChamberTimeFilter
 

class BestDoctorViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = (
        BestDoctor.objects
        .select_related('doctor_name', 'created_by')
    )
    serializer_class = BestDoctorSerializer



class DepartmentGroupViewSet(CreatedByMixin, viewsets.ModelViewSet):
    queryset = DepartmentGroup.objects.all()
    serializer_class = DepartmentGroupSerializer
    permission_classes = [AdminPermission]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['group_name']   # 👈 THIS ENABLES ?group_name=
    search_fields = ['group_name']

    def get_queryset(self):
        """
        Optimized queryset:
        - prefetch_related for ManyToMany
        - select_related for FK
        """

        return (
            DepartmentGroup.objects
            .select_related('created_by')          # FK
            .prefetch_related('departments')       # M2M ✅
            .all()
        )

# class DepartmentGroupListAPIView(ListAPIView):
#     queryset = DepartmentGroup.objects.all()
#     serializer_class = DepartmentGroupSerializer
#     permission_classes = [AdminPermission]


# class DepartmentGroupRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = DepartmentGroup.objects.all()
#     serializer_class = DepartmentGroupSerializer
#     permission_classes = [AdminPermission]
 