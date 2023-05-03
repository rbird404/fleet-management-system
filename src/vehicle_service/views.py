from common.views import APIViewSet
from vehicle_service.filters import ServiceIssueFilter
from vehicle_service.models import ServiceIssue, ServiceRecord, ServiceTask
from vehicle_service.serializers import *


class ServiceIssueViewSet(APIViewSet):
    queryset = ServiceIssue.objects.all()
    my_tags = ["service-issues"]
    filterset_class = ServiceIssueFilter

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return ServiceIssueListSerializer
            case 'retrieve':
                return ServiceIssueDisplaySerializer
            case _:
                return ServiceIssueDetailSerializer


class ServiceRecordViewSet(APIViewSet):
    queryset = ServiceRecord.objects.all()
    serializer_class = ServiceRecordDetailSerializer
    my_tags = ["service-records"]

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return ServiceIssueListSerializer
            case 'retrieve':
                return ServiceIssueDisplaySerializer
            case _:
                return ServiceIssueDetailSerializer


class ServiceTaskViewSet(APIViewSet):
    queryset = ServiceTask.objects.all()
    serializer_class = ServiceTaskSerializer
    my_tags = ["service-tasks"]
