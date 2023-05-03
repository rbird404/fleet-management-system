from django_filters import rest_framework as filters
from vehicles.models import Vehicle
from common.filters import BaseFilterSet


class VehicleFilter(BaseFilterSet):
    passport = filters.CharFilter(field_name='passport__number')
    sign = filters.CharFilter()
    subdivision = filters.NumberFilter(field_name='subdivision__pk')
    service = filters.NumberFilter(field_name='service__pk')
    exploitation_date = filters.DateFilter()

    class Meta:
        model = Vehicle
        fields = (
            'inventory_number',
            'year',
            'passport',
            'service',
            'sign',
            'subdivision',
            'manufacturer',
            'exploitation_date'
        )
