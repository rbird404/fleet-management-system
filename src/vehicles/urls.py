from rest_framework import routers

from vehicles.views import (
    VehicleViewSet, CounterViewset, VehicleTypeViewSet, VehicleBodyViewSet,
    ColorViewSet, VehicleClassViewSet,
    VehicleGroupViewSet, ManufacturerViewSet, SourceViewSet,
    MaintenanceServiceViewSet, WarehouseViewSet,
    SubdivisionViewSet, BrandViewSet, FuelTypeViewSet
)

router = routers.DefaultRouter()

router.register("types", VehicleTypeViewSet, basename='car_types')
router.register("bodies", VehicleBodyViewSet, basename='car_bodies')
router.register("colors", ColorViewSet, basename='car_colors')
router.register("classes", VehicleClassViewSet, basename="car_classes")
router.register("brands", BrandViewSet, basename="car_brands")
router.register("groups", VehicleGroupViewSet, basename="car_groups")
router.register("manufacturers", ManufacturerViewSet, basename="manufacturers")
router.register("sources", SourceViewSet, basename="sources")
router.register("services", MaintenanceServiceViewSet, basename="services")
router.register("warehouses", WarehouseViewSet, basename="warehouses")
router.register("subdivisions", SubdivisionViewSet, basename="subdivisions")
router.register("fuel-types", FuelTypeViewSet, basename="fuel-types")
router.register("counters", CounterViewset, basename='counters')
router.register("", VehicleViewSet, basename='vehicles')

urlpatterns = router.urls
