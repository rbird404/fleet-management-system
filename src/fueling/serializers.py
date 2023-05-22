from django.db.models import Max
from rest_framework import serializers

from fueling.models import Fueling
from common.serializers import BaseSerializer
from vehicles.serializers import VehicleListSerializer
from vehicles.models import Counter, Vehicle, FuelType
from vehicles.serializers import CounterCreateSerializer


class FuelingSerializer(BaseSerializer):
    vehicle = VehicleListSerializer(read_only=True)
    vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset=Vehicle.objects.all(), source='vehicle'
    )
    counter = CounterCreateSerializer()
    fuel_type_name = serializers.CharField(
        source='fuel_type.name', read_only=True
    )
    fuel_type = serializers.PrimaryKeyRelatedField(
        queryset=FuelType.objects.all()
    )
    current_counter = serializers.SerializerMethodField()
    date = serializers.DateTimeField(format="%Y-%m-%d")

    def get_current_counter(self, obj):
        result = Counter.objects.filter(
            vehicle=obj.vehicle
        ).aggregate(Max('value'))
        return result['value__max']

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
        counter_data = validated_data.get("counter")
        for attr, value in counter_data.items():
            setattr(counter, attr, value)
        counter.save()
        validated_data['counter'] = counter
        return super().update(instance, validated_data)

    class Meta:
        model = Fueling
        fields = "__all__"
