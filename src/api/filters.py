from django_filters import rest_framework as filters
from cars.models import Car


class CarFilter(filters.FilterSet):
    inventory_number = filters.NumberFilter()
    year = filters.NumberFilter()
    passport__number = filters.CharFilter()
    sign = filters.CharFilter()
    subdivision__pk = filters.NumberFilter()
    service__pk = filters.NumberFilter()
    exploitation_date = filters.DateFilter()

    class Meta:
        model = Car
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

    def filter_queryset(self, queryset):
        if (
                not self.request.user.is_superuser
                or not self.request.user.is_staff
        ):
            return queryset
        return queryset.active()
