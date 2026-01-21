from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Doctor, BestDoctor, Department, ChamberTime, DepartmentGroup, DepartmentBanner, DoctorBanner
from .serializers import DoctorSerializer, BestDoctorSerializer, DepartmentSerializer, ChamberTimeSerializer, DepartmentGroupSerializer, DepartmentBannerSerializer, DoctorBannerSerializer
from accounts.permissions import AdminPermission
from .filters import ChamberTimeFilter, DoctorFilter, DepartmentFilter
from .pagination import DoctorPagination, CustomPagination



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
    pagination_class = CustomPagination

    # 🔹 filter by department 'id', 'name', 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_class = DepartmentFilter



class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination
        

    # 🔹 filter by department slug
    filter_backends = [DjangoFilterBackend]
    filterset_class = DoctorFilter
    ordering = ['order']



    

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
 