from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from datetime import datetime

from common.views import APIViewSet
from maintenance.models import Task, Record, Issue
from maintenance.serializers import (
    TaskSerializer, IssueDetailSerializer, IssueListSerializer,
    RecordDetailSerializer, RecordListSerializer
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
    filterset_class = RecordFilter
    my_tags = ['maintenance']

    def get_serializer_class(self):
        if self.action == 'list':
            return RecordListSerializer
        return RecordDetailSerializer


class IssueAPI(APIViewSet):
    queryset = Issue.objects.all()
    filterset_class = IssueFilter
    my_tags = ['maintenance']

    def get_serializer_class(self):
        if self.action == 'list':
            return IssueListSerializer
        return IssueDetailSerializer

    @action(detail=True, methods=['post'])
    def close(self, request: Request, pk: int):
        now = datetime.now()
        instance: Issue = self.get_object()
        if now > instance.due_date:
            instance.status = "overdue"
        else:
            instance.status = "solved"
        instance.save()
        return Response(status=status.HTTP_200_OK)
