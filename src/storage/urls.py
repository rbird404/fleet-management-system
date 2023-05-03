from rest_framework import routers
from storage.views import FileViewSet, ImageViewSet

router = routers.DefaultRouter()

router.register("images", ImageViewSet, basename="images")
router.register("files", FileViewSet, basename="files")

urlpatterns = router.urls
