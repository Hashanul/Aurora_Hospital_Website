import django_filters
from .models import PatientStory



class PatientStoryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains'
    )

    department = django_filters.CharFilter(
        field_name='department__name',
        lookup_expr='icontains'
    )

    id = django_filters.NumberFilter(
        field_name='id'
    )

    class Meta:
        model = PatientStory
        fields = ['id', 'title', 'department']

