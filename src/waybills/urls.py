from rest_framework import routers

from waybills.views import WaybillAPI, FileAPI, ImageAPI

router = routers.DefaultRouter()

router.register("images", ImageAPI, basename="waybill-images")
router.register("files", FileAPI, basename="waybill-files")
router.register("", WaybillAPI, basename='waybills')

urlpatterns = router.urls
