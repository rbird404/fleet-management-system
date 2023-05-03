from common.serializers import BaseSerializer

from storage.models import Image, File


class ImageSerializer(BaseSerializer):
    class Meta:
        model = Image
        fields = (
            'id',
            'creator',
            'deleted_at',
            'updated_at',
            'created_at',
            'image',
        )


class FileSerializer(BaseSerializer):
    class Meta:
        model = File
        fields = (
            'id',
            'creator',
            'deleted_at',
            'updated_at',
            'created_at',
            'file',
        )
