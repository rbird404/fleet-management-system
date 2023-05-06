from common.views import APIViewSet
from fueling.filters import FuelingFilter
from fueling.models import Fueling
from fueling.serializers import FuelingSerializer


class FuelingAPI(APIViewSet):
    queryset = Fueling.objects.all()
    serializer_class = FuelingSerializer
    filterset_class = FuelingFilter
    my_tags = ['fueling']
