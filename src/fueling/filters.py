from django_filters import rest_framework as filters

from common.filters import BaseFilterSet, NumberInFilter
from fueling.models import Fueling


class FuelingFilter(BaseFilterSet):
    vehicle = NumberInFilter(field_name='vehicle__id', lookup_expr='in')
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = Fueling
        fields = ('vehicle', 'date')
