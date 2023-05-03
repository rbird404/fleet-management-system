from common.filters import BaseFilterSet
from django_filters import rest_framework as filters
from vehicle_service.models import ServiceIssue


class ServiceIssueFilter(BaseFilterSet):
    vehicle = filters.NumberFilter(field_name='vehicle__id')

    class Meta:
        model = ServiceIssue
        fields = ('vehicle', 'status')
