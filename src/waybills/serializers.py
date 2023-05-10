from rest_framework import serializers

from common.serializers import BaseSerializer
from vehicles.models import Vehicle
from waybills.models import Waybill, File, Image
from vehicles.serializers import VehicleListSerializer


class WaybillSerializer(BaseSerializer):
    vehicle = VehicleListSerializer(read_only=True)
    vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset=Vehicle.objects.all(), source='vehicle'
    )
    images = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(), required=False, many=True
    )
    files = serializers.PrimaryKeyRelatedField(
        queryset=File.objects.all(), required=False, many=True
    )
    date = serializers.DateField(format="%Y-%m-%d")

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

