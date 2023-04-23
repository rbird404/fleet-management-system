from rest_framework import routers

from cars.views import (
    CarTypeView, CarBodyView, CarClassView, CarGroupView,
    ColorView, ManufacturerView, BrandView,
    SourceView, MaintenanceServiceView, WarehouseView,
    WaybillView, GasolineBrandView, SubdivisionView,
    EngineView, PassportView, DistributionView, CarView
)


router = routers.DefaultRouter()

router.register("types", CarTypeView, basename='car_types')
router.register("bodies", CarBodyView, basename='car_bodies')
router.register("colors", ColorView, basename='car_colors')
router.register("classes", CarClassView, basename="car_classes")
router.register("brands", BrandView, basename="car_brands")
router.register("groups", CarGroupView, basename="car_groups")
router.register("manufacturer", ManufacturerView, basename="manufacturers")
router.register("gasolinebrands", GasolineBrandView, basename="gasolinebrands")
router.register("sources", SourceView, basename="sources")
router.register("services", MaintenanceServiceView, basename="services")
router.register("warehouses", WarehouseView, basename="warehouses")
router.register("passports", PassportView, basename="passports")
router.register("distributions", DistributionView, basename="distributions")
router.register("waybills", WaybillView, basename="waybills")
router.register("engines", EngineView, basename="engines")
router.register("subdivisions", SubdivisionView, basename="subdivisions")
router.register("", CarView, basename='cars')

urlpatterns = router.urls
