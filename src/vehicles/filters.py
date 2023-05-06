from django_filters import rest_framework as filters
from vehicles.models import Vehicle, Counter
from common.filters import BaseFilterSet


class VehicleFilter(BaseFilterSet):
    passport = filters.CharFilter(field_name='passport__number')
    gov_number = filters.CharFilter()
    subdivision = filters.NumberFilter(field_name='subdivision__pk')
    manufacturer = filters.NumberFilter(field_name='manufacturer__pk')
    service = filters.NumberFilter(field_name='service__pk')
    exploitation_date = filters.DateFilter()

    class Meta:
        model = Vehicle
        fields = (
            'inventory_number',
            'year',
            'passport',
            'service',
            'gov_number',
            'subdivision',
            'manufacturer',
            'exploitation_date'
        )


class CounterFilter(BaseFilterSet):
    vehicle = filters.NumberFilter(field_name='vehicle__id')

    class Meta:
        model = Counter
        fields = ('vehicle',)
