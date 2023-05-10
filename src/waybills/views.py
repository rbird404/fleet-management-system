from common.views import APIViewSet
from waybills.models import Waybill, Image, File
from waybills.serializers import (
    WaybillSerializer, ImageSerializer, FileSerializer,
)


class WaybillAPI(APIViewSet):
    queryset = Waybill.objects.all()
    serializer_class = WaybillSerializer
    my_tags = ['waybills']


class ImageAPI(APIViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    my_tags = ['waybills-media']


class FileAPI(APIViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    my_tags = ['waybills-media']
