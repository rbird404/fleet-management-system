from rest_framework import viewsets
from api.filters import CarFilter
from api.serializers import (
    CarCreateUpdateSerializer, CarListSerializer,
    CarDisplaySerializer, CarTypeSerializer, ManufacturerSerializer,
    BrandSerializer, CarBodySerializer, CarGroupSerializer,
    GasolineBrandSerializer, CarClassSerializer, ColorSerializer,
    MaintenanceServiceSerializer, SubdivisionSerializer,
    SourceSerializer, WarehouseSerializer
)
from cars.models import (
    Car, CarType, Brand, Manufacturer, CarBody, CarGroup,
    CarClass, GasolineBrand, Color, MaintenanceService,
    Subdivision, Source, Warehouse
)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    filterset_class = CarFilter

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return CarListSerializer
            case 'create' | 'update':
                return CarCreateUpdateSerializer
            case _:
                return CarDisplaySerializer


class CarTypeViewSet(viewsets.ModelViewSet):
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarBodyViewSet(viewsets.ModelViewSet):
    queryset = CarBody.objects.all()
    serializer_class = CarBodySerializer


class CarGroupViewSet(viewsets.ModelViewSet):
    queryset = CarGroup.objects.all()
    serializer_class = CarGroupSerializer


class GasolineBrandViewSet(viewsets.ModelViewSet):
    queryset = GasolineBrand.objects.all()
    serializer_class = GasolineBrandSerializer


class CarClassViewSet(viewsets.ModelViewSet):
    queryset = CarClass.objects.all()
    serializer_class = CarClassSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class MaintenanceServiceViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceService.objects.all()
    serializer_class = MaintenanceServiceSerializer


class SubdivisionViewSet(viewsets.ModelViewSet):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
