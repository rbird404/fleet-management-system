from django_filters import rest_framework as filters

from apps.cars.models import Car

class CarFilter(filters.FilterSet):
    inventory_number = filters.NumberFilter()
    year = filters.NumberFilter()
    passport__number = filters.CharFilter()
    sign = filters.CharFilter()
    owner__pk = filters.NumberFilter()
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
            'owner',
            'manufacturer',
            'exploitation_date'
        )