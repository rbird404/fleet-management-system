from common.serializers import BaseSerializer
from vehicle_service.models import ServiceIssue, ServiceRecord
from vehicles.models import Counter
from vehicles.serializers import CounterSerializer


class ServiceIssueSerializer(BaseSerializer):
    counter = CounterSerializer()

    def create(self, validated_data):
        validated_data['counter'] = Counter.objects.create(**validated_data.pop('counter'))
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


class ServiceRecordSerializer(BaseSerializer):
    class Meta:
        model = ServiceRecord
        fields = "__all__"
