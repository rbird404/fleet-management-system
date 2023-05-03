from rest_framework import viewsets

from common.mixins import DeactivateModelMixin
from common.models import BaseModel
from common.filters import BaseFilterSet
from common.serializers import BaseSerializer


class APIViewSet(DeactivateModelMixin, viewsets.ModelViewSet):
    queryset: BaseModel
    filterset_class: BaseFilterSet
    serializer_class: BaseSerializer
