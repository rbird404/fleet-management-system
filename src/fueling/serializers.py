from django.db.models import Max
from rest_framework import serializers

from fueling.models import Fueling
from common.serializers import BaseSerializer
from vehicles.serializers import VehicleListSerializer
from vehicles.models import Counter, Vehicle


class CounterCreateSerializer(BaseSerializer):
    id = serializers.IntegerField(read_only=True)
    value = serializers.IntegerField()

    class Meta:
        model = Counter
        fields = ('id', 'value')


class FuelingSerializer(BaseSerializer):
    vehicle = VehicleListSerializer(read_only=True)
    vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset=Vehicle.objects.all(), source='vehicle'
    )
    counter = CounterCreateSerializer()
    vehicle_current_counter_value = serializers.SerializerMethodField()

    def vehicle_current_counter_value(self, obj):
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
        counter.value = validated_data.get("counter").get('value')
        counter.save()
        validated_data['counter'] = counter
        return super().update(instance, validated_data)

    class Meta:
        model = Fueling
        fields = "__all__"
