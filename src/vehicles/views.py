from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from vehicles.services import HistoryService
from vehicles.filters import VehicleFilter
from common.views import APIViewSet
from vehicles.serializers import (
    VehicleDetailSerializer, VehicleListSerializer,
    VehicleDisplaySerializer, VehicleTypeSerializer, ManufacturerSerializer,
    BrandSerializer, VehicleBodySerializer, VehicleGroupSerializer,
    FuelTypeSerializer, VehicleClassSerializer, ColorSerializer,
    MaintenanceServiceSerializer, SubdivisionSerializer,
    SourceSerializer, WarehouseSerializer, HistorySerializer, VehicleFileSerializer,
    VehicleImageSerializer
)
from vehicles.models import (
    Vehicle, VehicleType, Brand, Manufacturer, VehicleBody, VehicleGroup,
    VehicleClass, FuelType, Color, MaintenanceService,
    Subdivision, Source, Warehouse, VehicleFile, VehicleImage
)


class VehicleAPI(APIViewSet):
    queryset = Vehicle.objects.all()
    filterset_class = VehicleFilter
    my_tags = ['vehicle']

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return VehicleListSerializer
            case 'create' | 'update':
                return VehicleDetailSerializer
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


class ImageAPI(APIViewSet):
    queryset = VehicleImage.objects.all()
    serializer_class = VehicleImageSerializer
    my_tags = ['vehicle-media']


class FileAPI(APIViewSet):
    queryset = VehicleFile.objects.all()
    serializer_class = VehicleFileSerializer
    my_tags = ['vehicle-media']


class VehicleTypeAPI(APIViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    my_tags = ['vehicle']


class ManufacturerAPI(APIViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    my_tags = ['vehicle']


class BrandAPI(APIViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    my_tags = ['vehicle']


class VehicleBodyAPI(APIViewSet):
    queryset = VehicleBody.objects.all()
    serializer_class = VehicleBodySerializer
    my_tags = ['vehicle']


class VehicleGroupAPI(APIViewSet):
    queryset = VehicleGroup.objects.all()
    serializer_class = VehicleGroupSerializer
    my_tags = ['vehicle']


class FuelTypeAPI(APIViewSet):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer
    my_tags = ['vehicle']


class VehicleClassAPI(APIViewSet):
    queryset = VehicleClass.objects.all()
    serializer_class = VehicleClassSerializer
    my_tags = ['vehicle']


class ColorAPI(APIViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    my_tags = ['vehicle']


class MaintenanceServiceAPI(APIViewSet):
    queryset = MaintenanceService.objects.all()
    serializer_class = MaintenanceServiceSerializer
    my_tags = ['vehicle']


class SubdivisionAPI(APIViewSet):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer
    my_tags = ['vehicle']


class SourceAPI(APIViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    my_tags = ['vehicle']


class WarehouseAPI(APIViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    my_tags = ['vehicle']
