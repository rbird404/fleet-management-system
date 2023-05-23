from django_filters import rest_framework as filters

from common.filters import BaseFilterSet, NumberInFilter
from waybills.models import Waybill


class WaybillFilter(BaseFilterSet):
    vehicle = NumberInFilter(field_name='vehicle__id', lookup_expr='in')
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = Waybill
        fields = ('vehicle', 'date')
