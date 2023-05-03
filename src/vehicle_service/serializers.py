from rest_framework import serializers

from common.serializers import BaseSerializer, BaseUserSerializer
from storage.models import Image, File
from storage.serializers import ImageSerializer, FileSerializer
from vehicle_service.models import ServiceIssue, ServiceRecord, ServiceTask
from vehicles.models import Counter
from vehicles.serializers import CounterSerializer, VehicleListSerializer


class ServiceTaskSerializer(BaseSerializer):
    class Meta:
        model = ServiceTask
        fields = "__all__"


class ServiceIssueListSerializer(BaseSerializer):
    vechicle = VehicleListSerializer()
    images = ImageSerializer(read_only=True, many=True)
    counter = serializers.IntegerField(source='counter.value')
    users = BaseUserSerializer(many=True)

    class Meta:
        model = ServiceIssue
        fields = '__all__'


class ServiceIssueDetailSerializer(BaseSerializer):
    counter = CounterSerializer()
    images = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(), required=False, many=True
    )
    files = serializers.PrimaryKeyRelatedField(
        queryset=File.objects.all(), required=False, many=True
    )

    def create(self, validated_data):
        validated_data['counter'] = Counter.objects.create(
            **validated_data.pop('counter')
        )
        return super().create(validated_data)

    def update(self, instance, validated_data):
        counter = instance.counter
        for attr, value in validated_data.pop('counter').items():
            setattr(counter, attr, value)
        counter.save()
        validated_data['counter'] = counter
        return super().update(instance, validated_data)

    class Meta:
        model = ServiceIssue
        fields = '__all__'


class ServiceIssueDisplaySerializer(ServiceIssueListSerializer):
    files = FileSerializer(read_only=True, many=True)
    creator = BaseUserSerializer()


class ServiceRecordDetailSerializer(ServiceIssueDetailSerializer):
    class Meta:
        model = ServiceRecord
        fields = "__all__"
