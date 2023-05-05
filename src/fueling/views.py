from common.views import APIViewSet
from fueling.models import Fueling
from fueling.serializers import FuelingSerializer


class FuelingAPI(APIViewSet):
    queryset = Fueling.objects.all()
    serializer_class = FuelingSerializer
    my_tags = ['fueling']
