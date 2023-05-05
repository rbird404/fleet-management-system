from common.filters import BaseFilterSet
from django_filters import rest_framework as filters
from maintenance.models import Task, Record, Issue


class TaskFilter(BaseFilterSet):
    vehicle = filters.NumberFilter(field_name='vehicle__id')

    class Meta:
        model = Task
        fields = ('vehicle',)


class RecordFilter(BaseFilterSet):
    vehicle = filters.NumberFilter(field_name='vehicle__id')

    class Meta:
        model = Record
        fields = ('vehicle',)


class IssueFilter(BaseFilterSet):
    vehicle = filters.NumberFilter(field_name='vehicle__id')

    class Meta:
        model = Issue
        fields = ('vehicle', 'status')
