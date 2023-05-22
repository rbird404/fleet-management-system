from django.db import models
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.request import Request
from rest_framework.response import Response

from common.serializers import BaseSerializer
from vehicles.services import HistoryService
from vehicles.filters import VehicleFilter, CounterFilter, ExpenseFilter
from common.views import APIViewSet
from vehicles.serializers import (
    VehicleDetailSerializer, VehicleListSerializer, HistorySerializer,
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
        elif self.action == 'history':
            return HistorySerializer

        return VehicleDetailSerializer

    @action(detail=True, methods=['get'])
    def history(self, request: Request, pk: int):
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


class ModelAPI(APIViewSet):
    mapping = {
        "types": VehicleType,
        "manufacturers": Manufacturer,
        "brands": Brand,
        "bodies": VehicleBody,
        "groups": VehicleGroup,
        "fuel-types": FuelType,
        "classes": VehicleClass,
        "colors": Color,
        "services": MaintenanceService,
        "subdivisions": Subdivision,
        "sources": Source,
        "warehouses": Warehouse,
    }

    def get_queryset(self):
        return self.get_model().objects.all()

    def get_serializer_class(self):
        model = self.get_model()
        return self.create_serializer_class(model, exclude=('code',))

    def get_model(self) -> models.Model:
        path: str = self.kwargs.get("path")
        model: models.Model = self.mapping.get(path)
        if model is not None:
            return model
        raise NotFound

    @staticmethod
    def create_serializer_class(
            model: models.Model,
            *,
            fields: str | list = None,
            exclude: tuple[str] = None
    ):
        meta_data = {"model": model}
        if fields is not None:
            meta_data["fields"] = fields
        elif exclude is not None:
            meta_data["exclude"] = exclude

        meta_class = type("Meta", (), meta_data)
        return type(f"{model.__name__}Serializer", (BaseSerializer,), {"Meta": meta_class})
