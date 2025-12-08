from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Doctor

class DoctorPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

    # Override paginate_queryset to control pagination using ?pagination=true
    def paginate_queryset(self, queryset, request, view=None):
        paginate = request.query_params.get('pagination', 'false').lower()

        # If pagination=true -> normal pagination
        if paginate == 'true':
            return super().paginate_queryset(queryset, request, view)

        # If no pagination -> return None (DRF will skip pagination)
        return None  

    # Custom response if paginated
    def get_paginated_response(self, data):
        return Response({
            "total_doctor": Doctor.objects.count(),  # 🔥 actual total in database
            "total": self.page.paginator.count,      # total considering filters (after filtering)
            "count": len(data),                      # items in this page
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data
        })
