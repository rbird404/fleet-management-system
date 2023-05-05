from common.views import APIViewSet
from waybills.models import Waybill, Image, File
from waybills.serializers import (
    WaybillDetailSerializer, ImageSerializer, FileSerializer,
    WaybillDisplaySerializer
)


class WaybillAPI(APIViewSet):
    queryset = Waybill.objects.all()
    my_tags = ['waybills']

    def get_serializer_class(self):
        if self.action in ('list', 'create'):
            return WaybillDisplaySerializer
        return WaybillDetailSerializer


class ImageAPI(APIViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    my_tags = ['waybills-media']


class FileAPI(APIViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    my_tags = ['waybills-media']
