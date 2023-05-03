from common.views import APIViewSet
from storage.models import Image, File
from storage.serializers import ImageSerializer, FileSerializer


class ImageViewSet(APIViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    my_tags = ["storage"]


class FileViewSet(APIViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    my_tags = ["storage"]
