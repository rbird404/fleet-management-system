from rest_framework import routers

from vehicles.views import (
    VehicleViewSet, CounterViewset, VehicleTypeViewSet, VehicleBodyViewSet,
    ColorViewSet, VehicleClassViewSet,
    VehicleGroupViewSet, ManufacturerViewSet, SourceViewSet,
    MaintenanceServiceViewSet, WarehouseViewSet,
    SubdivisionViewSet, BrandViewSet, FuelTypeViewSet
)

router = routers.DefaultRouter()

urlpatterns = router.urls
