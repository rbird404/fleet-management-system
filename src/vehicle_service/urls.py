from rest_framework import routers
from vehicle_service.views import (
    ServiceIssueViewSet, ServiceRecordViewSet, ServiceTaskViewSet
)

router = routers.DefaultRouter()

router.register("issues", ServiceIssueViewSet, basename="service_issues")
router.register("records", ServiceRecordViewSet, basename="service_records")
router.register("tasks", ServiceTaskViewSet, basename="service_tasks")

urlpatterns = router.urls
