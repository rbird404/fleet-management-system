from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from common.mixins import DeactivateModelMixin
from common.models import BaseModel
from common.filters import BaseFilterSet
from common.serializers import BaseSerializer


class APIViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    DeactivateModelMixin,
    GenericViewSet
):
    queryset: BaseModel
    filterset_class = BaseFilterSet
    serializer_class: BaseSerializer
