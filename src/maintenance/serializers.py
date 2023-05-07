from rest_framework import serializers

from common.serializers import BaseSerializer, BaseUserSerializer
from fueling.serializers import CounterCreateSerializer
from maintenance.models import Record, Issue, Task
from vehicles.models import Vehicle, Counter
from vehicles.serializers import VehicleListSerializer


class TaskSerializer(BaseSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class IssueListSerializer(BaseSerializer):
    vehicle = VehicleListSerializer()
    users = BaseUserSerializer(many=True)
    counter = CounterCreateSerializer()

    class Meta:
        model = Issue
        fields = '__all__'


class IssueDetailSerializer(BaseSerializer):
    vehicle = VehicleListSerializer(read_only=True)
    vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset=Vehicle.objects.all(), source='vehicle'
    )
    counter = CounterCreateSerializer()

    def create(self, validated_data):
        counter_data = validated_data.get("counter")
        counter = Counter.objects.create(
            vehicle=validated_data.get("vehicle"),
            date=validated_data.get("date"),
            **counter_data,
        )
        validated_data['counter'] = counter
        return super().create(validated_data)

    def update(self, instance, validated_data):
        counter = instance.counter
        counter.value = validated_data.get("counter").get('value')
        counter.save()
        validated_data['counter'] = counter
        return super().update(instance, validated_data)

    class Meta:
        model = Issue
        fields = '__all__'


class RecordSerializer(BaseSerializer):
    vehicle = VehicleListSerializer(read_only=True)
    vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset=Vehicle.objects.all(), source='vehicle'
    )

    class Meta:
        model = Record
        fields = '__all__'
