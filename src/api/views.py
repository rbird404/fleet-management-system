from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from api.filters import CarFilter
from cars.models import Car
from api.serializers import (
    CarCreateUpdateSerializer,
    CarListSerializer,
    CarDisplaySerializer
)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return CarListSerializer

            case 'create' | 'update':
                return CarCreateUpdateSerializer

            case _:
                return CarDisplaySerializer
