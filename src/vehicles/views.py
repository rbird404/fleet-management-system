from typing import Optional

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from vehicles.services import HistoryService
from vehicles.filters import VehicleFilter, CounterFilter, ExpenseFilter
from common.views import APIViewSet
from vehicles.serializers import (
    VehicleDetailSerializer, VehicleListSerializer,
    VehicleDisplaySerializer, VehicleTypeSerializer, ManufacturerSerializer,
    BrandSerializer, VehicleBodySerializer, VehicleGroupSerializer,
    FuelTypeSerializer, VehicleClassSerializer, ColorSerializer,
    MaintenanceServiceSerializer, SubdivisionSerializer,
    SourceSerializer, WarehouseSerializer, HistorySerializer,
    VehicleFileSerializer, VehicleImageSerializer, CounterSerializer,
    ExpenseSerializer, ExpenseListSerializer, ExpenseTypeSerializer
)
from vehicles.models import (
    Vehicle, VehicleType, Brand, Manufacturer, VehicleBody, VehicleGroup,
    VehicleClass, FuelType, Color, MaintenanceService,
    Subdivision, Source, Warehouse, VehicleFile, VehicleImage, Counter,
    ExpenseType, Expense
)


class VehicleAPI(APIViewSet):
    queryset = Vehicle.objects.all()
    filterset_class = VehicleFilter
    my_tags = ['vehicle']

    def get_serializer_class(self):
        if self.action == "list":
            return VehicleListSerializer
        elif self.action in ('create', 'update'):
            return VehicleDetailSerializer
        elif self.action == 'history':
            return HistorySerializer

        return VehicleDisplaySerializer

    @action(detail=True, methods=['get'])
    def history(self, request: Request, pk: Optional[int]):
        vehicle: Vehicle = self.get_object()
        field: str = request.query_params.get('field')
        history_service = HistoryService(vehicle)
        qs = history_service.get_history(field)
        data = HistorySerializer(qs, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class CounterAPI(APIViewSet):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer
    my_tags = ['counter']
    filterset_class = CounterFilter


class ImageAPI(APIViewSet):
    queryset = VehicleImage.objects.all()
    serializer_class = VehicleImageSerializer
    my_tags = ['vehicle media']


class FileAPI(APIViewSet):
    queryset = VehicleFile.objects.all()
    serializer_class = VehicleFileSerializer
    my_tags = ['vehicle media']


class VehicleTypeAPI(APIViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    my_tags = ['vehicle types']


class ManufacturerAPI(APIViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    my_tags = ['vehicle manufacturers']


class BrandAPI(APIViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    my_tags = ['vehicle brands']


class VehicleBodyAPI(APIViewSet):
    queryset = VehicleBody.objects.all()
    serializer_class = VehicleBodySerializer
    my_tags = ['vehicle bodies']


class VehicleGroupAPI(APIViewSet):
    queryset = VehicleGroup.objects.all()
    serializer_class = VehicleGroupSerializer
    my_tags = ['vehicle groups']


class FuelTypeAPI(APIViewSet):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer
    my_tags = ['vehicle fuel-types']


class VehicleClassAPI(APIViewSet):
    queryset = VehicleClass.objects.all()
    serializer_class = VehicleClassSerializer
    my_tags = ['vehicle classes']


class ColorAPI(APIViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    my_tags = ['vehicle colors']


class MaintenanceServiceAPI(APIViewSet):
    queryset = MaintenanceService.objects.all()
    serializer_class = MaintenanceServiceSerializer
    my_tags = ['vehicle services']


class SubdivisionAPI(APIViewSet):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer
    my_tags = ['vehicle subdivisions']


class SourceAPI(APIViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    my_tags = ['vehicle sources']


class WarehouseAPI(APIViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    my_tags = ['vehicle warehouses']


class ExpenseTypeAPI(APIViewSet):
    queryset = ExpenseType.objects.all()
    serializer_class = ExpenseTypeSerializer
    my_tags = ['expenses']


class ExpenseAPI(APIViewSet):
    queryset = Expense.objects.all()
    my_tags = ['expenses']
    filterset_class = ExpenseFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ExpenseListSerializer
        return ExpenseSerializer
