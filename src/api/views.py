from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from api.services import HistoryService
from api.filters import CarFilter
from api.mixins import DeactivateModelMixin
from api.serializers import (
    CarCreateUpdateSerializer, CarListSerializer,
    CarDisplaySerializer, CarTypeSerializer, ManufacturerSerializer,
    BrandSerializer, CarBodySerializer, CarGroupSerializer,
    GasolineBrandSerializer, CarClassSerializer, ColorSerializer,
    MaintenanceServiceSerializer, SubdivisionSerializer,
    SourceSerializer, WarehouseSerializer, HistorySerializer
)
from cars.models import (
    Car, CarType, Brand, Manufacturer, CarBody, CarGroup,
    CarClass, GasolineBrand, Color, MaintenanceService,
    Subdivision, Source, Warehouse
)


class CarViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = Car.objects.all()
    filterset_class = CarFilter

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return CarListSerializer
            case 'create' | 'update':
                return CarCreateUpdateSerializer
            case 'history':
                return HistorySerializer
            case _:
                return CarDisplaySerializer

    @action(detail=True, methods=['get'])
    def history(self, request: Request, pk: int | None):
        car: Car = self.get_object()
        field: str = request.query_params.get('field')
        history_service = HistoryService(car)
        qs = history_service.get_history(field)
        data = HistorySerializer(qs, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class CarTypeViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer


class ManufacturerViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class BrandViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarBodyViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = CarBody.objects.all()
    serializer_class = CarBodySerializer


class CarGroupViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = CarGroup.objects.all()
    serializer_class = CarGroupSerializer


class GasolineBrandViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = GasolineBrand.objects.all()
    serializer_class = GasolineBrandSerializer


class CarClassViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = CarClass.objects.all()
    serializer_class = CarClassSerializer


class ColorViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class MaintenanceServiceViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = MaintenanceService.objects.all()
    serializer_class = MaintenanceServiceSerializer


class SubdivisionViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer


class SourceViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class WarehouseViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
