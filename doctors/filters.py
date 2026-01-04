
import django_filters
from .models import ChamberTime, Doctor

class ChamberTimeFilter(django_filters.FilterSet):
    dayName = django_filters.CharFilter(field_name='dayName', lookup_expr='icontains')
    # drCode = django_filters.ModelChoiceFilter(queryset=Doctor.objects.all())
    drCode = django_filters.CharFilter(field_name="drCode__drCode", lookup_expr='icontains')

    drName = django_filters.CharFilter(field_name='drCode__drName', lookup_expr='icontains')

    class Meta:
        model = ChamberTime
        fields = ['dayName', 'drCode', 'drName']



class DoctorFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(
        field_name='department__slug',   # বা department__name
        lookup_expr='icontains'
    )

    # 🔹 filter by department id
    department_id = django_filters.NumberFilter(
        field_name='department_id'
    )

    drName = django_filters.CharFilter(
        field_name='drName',
        lookup_expr='icontains'
    )

    class Meta:
        model = Doctor
        fields = ['department', 'department_id', 'drName']
