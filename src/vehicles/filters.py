from django_filters import rest_framework as filters
from vehicles.models import Vehicle, Counter, Expense
from common.filters import BaseFilterSet, NumberInFilter


class VehicleFilter(BaseFilterSet):
    inventory_number = NumberInFilter(lookup_expr='in')
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
    vehicle = NumberInFilter(field_name='vehicle__id', lookup_expr='in')
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = Counter
        fields = ('vehicle', 'date')


class ExpenseFilter(BaseFilterSet):
    vehicle = NumberInFilter(field_name='vehicle__id', lookup_expr='in')
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = Expense
        fields = ('vehicle', 'date')
