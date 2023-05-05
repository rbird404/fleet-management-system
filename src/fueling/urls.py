from rest_framework.routers import DefaultRouter
from fueling.views import FuelingAPI

router = DefaultRouter()

router.register("", FuelingAPI, basename="fueling")

urlpatterns = router.urls
