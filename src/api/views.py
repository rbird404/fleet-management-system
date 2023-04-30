from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from api.services import HistoryService
from api.filters import VehicleFilter
from api.mixins import DeactivateModelMixin
from api.serializers import (
    VehicleCreateUpdateSerializer, VehicleListSerializer,
    VehicleDisplaySerializer, VehicleTypeSerializer, ManufacturerSerializer,
    BrandSerializer, VehicleBodySerializer, VehicleGroupSerializer,
    GasolineBrandSerializer, VehicleClassSerializer, ColorSerializer,
    MaintenanceServiceSerializer, SubdivisionSerializer,
    SourceSerializer, WarehouseSerializer, HistorySerializer
)
from vehicles.models import (
    Vehicle, VehicleType, Brand, Manufacturer, VehicleBody, VehicleGroup,
    VehicleClass, FuelType, Color, MaintenanceService,
    Subdivision, Source, Warehouse
)


class VehicleViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    filterset_class = VehicleFilter

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return VehicleListSerializer
            case 'create' | 'update':
                return VehicleCreateUpdateSerializer
            case 'history':
                return HistorySerializer
            case _:
                return VehicleDisplaySerializer

    @action(detail=True, methods=['get'])
    def history(self, request: Request, pk: int | None):
        car: Vehicle = self.get_object()
        field: str = request.query_params.get('field')
        history_service = HistoryService(car)
        qs = history_service.get_history(field)
        data = HistorySerializer(qs, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class VehicleTypeViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class ManufacturerViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class BrandViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class VehicleBodyViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = VehicleBody.objects.all()
    serializer_class = VehicleBodySerializer


class VehicleGroupViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = VehicleGroup.objects.all()
    serializer_class = VehicleGroupSerializer


class GasolineBrandViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = FuelType.objects.all()
    serializer_class = GasolineBrandSerializer


class VehicleClassViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset = VehicleClass.objects.all()
    serializer_class = VehicleClassSerializer


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
