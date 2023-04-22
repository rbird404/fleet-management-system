from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from cars.filters import CarFilter
from cars.models import (
    CarType, CarBody, CarClass, CarGroup, Color, Manufacturer, Brand, Source,
    MaintenanceService, Warehouse, Waybill, GasolineBrand, Subdivision, Engine,
    Passport, Distribution, Car
)
from cars.serializers import (
    CarTypeSerializer, CarBodySerializer, CarClassSerializer,
    CarGroupSerializer, ColorSerializer, ManufacturerSerializer,
    BrandSerializer, SourceSerializer, MaintenanceServiceSerializer,
    WarehouseSerializer, WaybillSerializer, GasolineBrandSerializer,
    SubdivisionSerializer, EngineSerializer, PassportSerializer,
    DistributionSerializer, CarDetailSerializer
)


class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter


class CarTypeView(ModelViewSet):
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer


class ManufacturerView(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarBodyView(ModelViewSet):
    queryset = CarBody.objects.all()
    serializer_class = CarBodySerializer


class CarGroupView(ModelViewSet):
    queryset = CarGroup.objects.all()
    serializer_class = CarGroupSerializer


class GasolineBrandView(ModelViewSet):
    queryset = GasolineBrand.objects.all()
    serializer_class = GasolineBrandSerializer


class CarClassView(ModelViewSet):
    queryset = CarClass.objects.all()
    serializer_class = CarClassSerializer


class ColorView(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class MaintenanceServiceView(ModelViewSet):
    queryset = MaintenanceService.objects.all()
    serializer_class = MaintenanceServiceSerializer


class SubdivisionView(ModelViewSet):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer


class SourceView(ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class WarehouseView(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class EngineView(ModelViewSet):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer


class WaybillView(ModelViewSet):
    queryset = Waybill.objects.all()
    serializer_class = WaybillSerializer


class DistributionView(ModelViewSet):
    queryset = Distribution.objects.all()
    serializer_class = DistributionSerializer


class PassportView(ModelViewSet):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer
