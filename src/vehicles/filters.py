from django_filters import rest_framework as filters
from vehicles.models import Vehicle
from common.filters import BaseFilterSet


class VehicleFilter(BaseFilterSet):
    inventory_number = filters.NumberFilter()
    year = filters.NumberFilter()
    passport__number = filters.CharFilter()
    sign = filters.CharFilter()
    subdivision__pk = filters.NumberFilter()
    service__pk = filters.NumberFilter()
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
