from common.views import APIViewSet
from maintenance.models import Task, Record, Issue
from maintenance.serializers import (
    TaskSerializer, IssueDetailSerializer, IssueListSerializer, RecordSerializer
)
from maintenance.filters import (
    IssueFilter, RecordFilter
)


class TaskAPI(APIViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    my_tags = ['maintenance']


class RecordAPI(APIViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filterset_class = RecordFilter
    my_tags = ['maintenance']


class IssueAPI(APIViewSet):
    queryset = Issue.objects.all()
    filterset_class = IssueFilter
    my_tags = ['maintenance']

    def get_serializer_class(self):
        if self.action == 'list':
            return IssueListSerializer
        return IssueDetailSerializer
