from rest_framework import serializers

from common.serializers import BaseSerializer
from waybills.models import Waybill, File, Image
from vehicles.serializers import VehicleListSerializer


class WaybillDetailSerializer(BaseSerializer):
    images = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(), required=False, many=True
    )
    files = serializers.PrimaryKeyRelatedField(
        queryset=File.objects.all(), required=False, many=True
    )
    date = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Waybill
        fields = "__all__"


class ImageSerializer(BaseSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class FileSerializer(BaseSerializer):
    class Meta:
        model = File
        fields = "__all__"


class WaybillDisplaySerializer(BaseSerializer):
    vehicle = VehicleListSerializer()
    images = ImageSerializer(many=True)
    files = FileSerializer(many=True)

    class Meta:
        model = Waybill
        fields = "__all__"
