import django_filters
from .models import ChamberTime

class ChamberTimeFilter(django_filters.FilterSet):
    drCode = django_filters.CharFilter(field_name="drCode__drCode", lookup_expr='exact')

    class Meta:
        model = ChamberTime
        fields = ['drCode']
