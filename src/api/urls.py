from rest_framework import routers

from api.views import (
    CarBodyViewSet, CarTypeViewSet, ColorViewSet,
    CarClassViewSet, BrandViewSet, CarGroupViewSet,
    MaintenanceServiceViewSet, ManufacturerViewSet,
    GasolineBrandViewSet, SourceViewSet, WarehouseViewSet,
    SubdivisionViewSet, CarViewSet
)

router = routers.DefaultRouter()
router.register("types", CarTypeViewSet, basename='car_types')
router.register("bodies", CarBodyViewSet, basename='car_bodies')
router.register("colors", ColorViewSet, basename='car_colors')
router.register("classes", CarClassViewSet, basename="car_classes")
router.register("brands", BrandViewSet, basename="car_brands")
router.register("groups", CarGroupViewSet, basename="car_groups")
router.register("manufacturers", ManufacturerViewSet, basename="manufacturers")
router.register("sources", SourceViewSet, basename="sources")
router.register("services", MaintenanceServiceViewSet, basename="services")
router.register("warehouses", WarehouseViewSet, basename="warehouses")
router.register("subdivisions", SubdivisionViewSet, basename="subdivisions")
router.register("cars", CarViewSet, basename='cars')
router.register(
    "gasolinebrands", GasolineBrandViewSet, basename="gasolinebrands"
)

urlpatterns = router.urls
