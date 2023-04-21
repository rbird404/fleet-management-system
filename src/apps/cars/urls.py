from rest_framework import routers
from apps.cars.views import *


router = routers.DefaultRouter()

router.register("types", CarTypeView, basename='car_types')
router.register("bodies", CarBodyView, basename='car_bodies')
router.register("colors", ColorView, basename='car_colors')
router.register("classes", CarClassView, basename="car_classes")
router.register("brands", BrandView, basename="car_brans")
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
router.register("structures", StructureView, basename="structures")
router.register("", CarView, basename='cars')

urlpatterns = router.urls
