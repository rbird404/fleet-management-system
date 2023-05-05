from maintenance.views import TaskAPI, RecordAPI, IssueAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("tasks", TaskAPI, basename="service-tasks")
router.register("records", RecordAPI, basename="service-records")
router.register("issues", IssueAPI, basename="service-issues")

urlpatterns = router.urls
