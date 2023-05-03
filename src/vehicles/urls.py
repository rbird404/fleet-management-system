from rest_framework import routers

from vehicles.views import (
    VehicleBodyViewSet, VehicleTypeViewSet, ColorViewSet,
    VehicleClassViewSet, BrandViewSet, VehicleGroupViewSet,
    MaintenanceServiceViewSet, ManufacturerViewSet,
    FuelTypeViewSet, SourceViewSet, WarehouseViewSet,
    SubdivisionViewSet, VehicleViewSet
)

router = routers.DefaultRouter()

router.register(
    "fuel-types", FuelTypeViewSet, basename="fuel-types"
)
router.register("types", VehicleTypeViewSet, basename='vehicle_types')
router.register("bodies", VehicleBodyViewSet, basename='vehicle_bodies')
router.register("colors", ColorViewSet, basename='vehicle_colors')
router.register("classes", VehicleClassViewSet, basename="vehicle_classes")
router.register("brands", BrandViewSet, basename="vehicle_brands")
router.register("groups", VehicleGroupViewSet, basename="vehicle_groups")
router.register("manufacturers", ManufacturerViewSet, basename="manufacturers")
router.register("sources", SourceViewSet, basename="sources")
router.register("services", MaintenanceServiceViewSet, basename="services")
router.register("warehouses", WarehouseViewSet, basename="warehouses")
router.register("subdivisions", SubdivisionViewSet, basename="subdivisions")
router.register("", VehicleViewSet, basename='vehicles')


urlpatterns = router.urls
