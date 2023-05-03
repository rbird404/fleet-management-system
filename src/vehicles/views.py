from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from common.views import APIViewSet
from vehicles.services import HistoryService
from vehicles.filters import VehicleFilter, CounterFilter
from vehicles.serializers import (
    VehicleCreateUpdateSerializer, VehicleListSerializer,
    VehicleDisplaySerializer, VehicleTypeSerializer, ManufacturerSerializer,
    BrandSerializer, VehicleBodySerializer, VehicleGroupSerializer,
    FuelTypeSerializer, VehicleClassSerializer, ColorSerializer,
    MaintenanceServiceSerializer, SubdivisionSerializer,
    SourceSerializer, WarehouseSerializer, HistorySerializer, CounterSerializer
)
from vehicles.models import (
    Vehicle, VehicleType, Brand, Manufacturer, VehicleBody, VehicleGroup,
    VehicleClass, FuelType, Color, MaintenanceService,
    Subdivision, Source, Warehouse, Counter
)


class VehicleViewSet(APIViewSet):
    queryset = Vehicle.objects.all()
    filterset_class = VehicleFilter
    my_tags = ["vehicle"]

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


class CounterViewset(APIViewSet):
    queryset = Counter.objects.all()
    filterset_class = CounterFilter
    serializer_class = CounterSerializer
    my_tags = ["vehicle-counter"]


class VehicleTypeViewSet(APIViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    my_tags = ["vehicle-type"]


class ManufacturerViewSet(APIViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    my_tags = ["vehicle-manufacturer"]


class BrandViewSet(APIViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    my_tags = ["vehicle-brand"]


class VehicleBodyViewSet(APIViewSet):
    queryset = VehicleBody.objects.all()
    serializer_class = VehicleBodySerializer
    my_tags = ["vehicle-body"]


class VehicleGroupViewSet(APIViewSet):
    queryset = VehicleGroup.objects.all()
    serializer_class = VehicleGroupSerializer
    my_tags = ["vehicle-group"]


class FuelTypeViewSet(APIViewSet):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer
    my_tags = ["vehicle-fueltype"]


class VehicleClassViewSet(APIViewSet):
    queryset = VehicleClass.objects.all()
    serializer_class = VehicleClassSerializer
    my_tags = ["vehicle-class"]


class ColorViewSet(APIViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    my_tags = ["vehicle-color"]


class MaintenanceServiceViewSet(APIViewSet):
    queryset = MaintenanceService.objects.all()
    serializer_class = MaintenanceServiceSerializer
    my_tags = ["vehicle-service"]


class SubdivisionViewSet(APIViewSet):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer
    my_tags = ["vehicle-subdivision"]


class SourceViewSet(APIViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    my_tags = ["vehicle-source"]


class WarehouseViewSet(APIViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    my_tags = ["vehicle-warehouse"]
