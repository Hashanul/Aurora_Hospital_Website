
import django_filters
from .models import ChamberTime

class ChamberTimeFilter(django_filters.FilterSet):
    dayName = django_filters.CharFilter(field_name='dayName', lookup_expr='icontains')
    # drCode = django_filters.ModelChoiceFilter(queryset=Doctor.objects.all())
    drCode = django_filters.CharFilter(field_name="drCode__drCode", lookup_expr='icontains')

    drName = django_filters.CharFilter(field_name='drCode__drName', lookup_expr='icontains')

    class Meta:
        model = ChamberTime
        fields = ['dayName', 'drCode', 'drName']
