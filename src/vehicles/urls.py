from rest_framework import routers
from vehicles.views import (
    VehicleAPI, ImageAPI, FileAPI, CounterAPI,
    ExpenseAPI, ExpenseTypeAPI, ModelAPI
)

router = routers.DefaultRouter()

router.register(
    "expenses-types", ExpenseTypeAPI, basename='vehicle-expenses-types'
)
router.register("counters", CounterAPI, basename="counters")
router.register("images", ImageAPI, basename="vehicle-images")
router.register("files", FileAPI, basename="vehicle-files")
router.register("expenses", ExpenseAPI, basename='vehicle-expenses')
router.register("(?P<path>[a-z]+-?[a-z]*)", ModelAPI, basename="test")
router.register("", VehicleAPI, basename='vehicles')

urlpatterns = router.urls
