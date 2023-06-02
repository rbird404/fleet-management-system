from django_filters.rest_framework import filters

from common.filters import BaseFilterSet
from vehicles.models import Vehicle, Expense
from maintenance.models import Record


class ExpenseFilter(BaseFilterSet):
    date = filters.DateFromToRangeFilter(field_name='date')

    class Meta:
        model = Expense
        fields = ('date',)


class RecordFilter(BaseFilterSet):
    date = filters.DateFromToRangeFilter(field_name='end_date')

    class Meta:
        model = Record
        fields = ('date',)


class VehicleFilter(BaseFilterSet):
    vehicle = filters.NumberFilter(field_name='id')

    class Meta:
        model = Vehicle
        fields = ('vehicle',)
