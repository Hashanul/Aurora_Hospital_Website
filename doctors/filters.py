
import django_filters
from .models import ChamberTime, Doctor, Department
from home.models import Health_package

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
        field_name='department__slug',   # or department__name
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


class DepartmentFilter(django_filters.FilterSet):
    # name filter (partial search)
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains'
    )

    # slug filter
    slug = django_filters.CharFilter(
        field_name='slug',
        lookup_expr='iexact'
    )

    # id filter
    id = django_filters.NumberFilter(
        field_name='id'
    )

    class Meta:
        model = Department
        fields = ['id', 'name', 'slug']


class Health_packageFilter(django_filters.FilterSet):
    # title filter (partial search)
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains'
    )

    # slug filter
    slug = django_filters.CharFilter(
        field_name='slug',
        lookup_expr='iexact'
    )

    # id filter
    id = django_filters.NumberFilter(
        field_name='id'
    )

    class Meta:
        model = Health_package
        fields = ['id', 'title', 'slug']
