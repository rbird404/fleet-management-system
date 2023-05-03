from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from vehicles.services import HistoryService
from vehicles.filters import VehicleFilter
from common.views import APIViewSet
from vehicles.serializers import (
    VehicleCreateUpdateSerializer, VehicleListSerializer,
    VehicleDisplaySerializer, VehicleTypeSerializer, ManufacturerSerializer,
    BrandSerializer, VehicleBodySerializer, VehicleGroupSerializer,
    FuelTypeSerializer, VehicleClassSerializer, ColorSerializer,
    MaintenanceServiceSerializer, SubdivisionSerializer,
    SourceSerializer, WarehouseSerializer, HistorySerializer
)
from vehicles.models import (
    Vehicle, VehicleType, Brand, Manufacturer, VehicleBody, VehicleGroup,
    VehicleClass, FuelType, Color, MaintenanceService,
    Subdivision, Source, Warehouse
)


class VehicleViewSet(APIViewSet):
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
        vehicle: Vehicle = self.get_object()
        field: str = request.query_params.get('field')
        history_service = HistoryService(vehicle)
        qs = history_service.get_history(field)
        data = HistorySerializer(qs, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class VehicleTypeViewSet(APIViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class ManufacturerViewSet(APIViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class BrandViewSet(APIViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class VehicleBodyViewSet(APIViewSet):
    queryset = VehicleBody.objects.all()
    serializer_class = VehicleBodySerializer


class VehicleGroupViewSet(APIViewSet):
    queryset = VehicleGroup.objects.all()
    serializer_class = VehicleGroupSerializer


class FuelTypeViewSet(APIViewSet):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer


class VehicleClassViewSet(APIViewSet):
    queryset = VehicleClass.objects.all()
    serializer_class = VehicleClassSerializer


class ColorViewSet(APIViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class MaintenanceServiceViewSet(APIViewSet):
    queryset = MaintenanceService.objects.all()
    serializer_class = MaintenanceServiceSerializer


class SubdivisionViewSet(APIViewSet):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer


class SourceViewSet(APIViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class WarehouseViewSet(APIViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
