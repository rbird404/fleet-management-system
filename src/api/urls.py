from rest_framework import routers

from api.views import (
    VehicleBodyViewSet, VehicleTypeViewSet, ColorViewSet,
    VehicleClassViewSet, BrandViewSet, VehicleGroupViewSet,
    MaintenanceServiceViewSet, ManufacturerViewSet,
    GasolineBrandViewSet, SourceViewSet, WarehouseViewSet,
    SubdivisionViewSet, VehicleViewSet
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
router.register("vehicles", VehicleViewSet, basename='vehicles')
router.register(
    "gasolinebrands", GasolineBrandViewSet, basename="gasolinebrands"
)

urlpatterns = router.urls
