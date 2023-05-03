from rest_framework import routers

from vehicles.views import (
    VehicleBodyAPI, VehicleTypeAPI, ColorAPI,
    VehicleClassAPI, BrandAPI, VehicleGroupAPI,
    MaintenanceServiceAPI, ManufacturerAPI,
    FuelTypeAPI, SourceAPI, WarehouseAPI,
    SubdivisionAPI, VehicleAPI, ImageAPI, FileAPI
)

router = routers.DefaultRouter()

router.register(
    "fuel-types", FuelTypeAPI, basename="fuel-types"
)
router.register("types", VehicleTypeAPI, basename='vehicle-types')
router.register("bodies", VehicleBodyAPI, basename='vehicle-bodies')
router.register("colors", ColorAPI, basename='vehicle-colors')
router.register("classes", VehicleClassAPI, basename="vehicle-classes")
router.register("brands", BrandAPI, basename="vehicle-brands")
router.register("groups", VehicleGroupAPI, basename="vehicle-groups")
router.register("manufacturers", ManufacturerAPI, basename="manufacturers")
router.register("sources", SourceAPI, basename="sources")
router.register("services", MaintenanceServiceAPI, basename="services")
router.register("warehouses", WarehouseAPI, basename="warehouses")
router.register("subdivisions", SubdivisionAPI, basename="subdivisions")
router.register("images", ImageAPI, basename="vehicle-images")
router.register("files", FileAPI, basename="vehicle-files")
router.register("", VehicleAPI, basename='vehicles')

urlpatterns = router.urls
