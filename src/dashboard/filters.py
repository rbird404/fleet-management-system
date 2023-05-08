from django_filters.rest_framework import filters
from common.filters import BaseFilterSet
from vehicles.models import Vehicle


class CounterFilter(BaseFilterSet):
    date = filters.DateFromToRangeFilter()


class VehicleFilter(BaseFilterSet):
    vehicle = filters.NumberFilter(field_name='id')

    class Meta:
        model = Vehicle
        fields = ('vehicle',)
