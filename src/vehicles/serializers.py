from collections import OrderedDict
from typing import Optional

from rest_framework import serializers

from common.serializers import BaseSerializer
from vehicles.models import (
    Engine, Passport, Distribution, Vehicle,
    VehicleType, Brand, Manufacturer, VehicleBody, VehicleGroup,
    VehicleClass, FuelType, Color, MaintenanceService,
    Subdivision, Source, Warehouse, VehicleImage, VehicleFile, Counter
)
from history.models import History
from vehicles.models import ExpenseType, Expense


class VehicleImageSerializer(BaseSerializer):
    class Meta:
        model = VehicleImage
        fields = "__all__"


class VehicleFileSerializer(BaseSerializer):
    class Meta:
        model = VehicleFile
        fields = "__all__"


class EngineSerializer(BaseSerializer):
    class Meta:
        model = Engine
        fields = '__all__'


class DistributionSerializer(BaseSerializer):
    class Meta:
        model = Distribution
        fields = '__all__'


class PassportSerializer(BaseSerializer):
    class Meta:
        model = Passport
        fields = '__all__'


class VehicleDetailSerializer(BaseSerializer):
    engine = EngineSerializer()
    distribution = DistributionSerializer()
    passport = PassportSerializer()
    images = serializers.PrimaryKeyRelatedField(
        queryset=VehicleImage.objects.all(), required=False, many=True
    )
    files = serializers.PrimaryKeyRelatedField(
        queryset=VehicleFile.objects.all(), required=False, many=True
    )

    def create(self, validated_data: OrderedDict) -> Vehicle:
        nested_fields = {}
        for field, data in validated_data.items():
            if isinstance(data, OrderedDict):
                nested_fields[field] = (
                    self.fields[field].Meta.model.objects.create(**data)
                )
        validated_data.update(nested_fields)
        return super().create(validated_data)

    def update(self, instance: Vehicle, validated_data: OrderedDict) -> Vehicle:
        nested_fields = {}
        for field, value in validated_data.items():
            if isinstance(value, OrderedDict):
                obj = getattr(instance, field)
                for obj_attr, obj_value in value.items():
                    setattr(obj, obj_attr, obj_value)
                obj.save()
                value = obj

            nested_fields[field] = value
        validated_data.update(nested_fields)
        return super().update(instance, validated_data)

    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleListSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source="brand.name", allow_null=True)
    group = serializers.CharField(source='group.name', allow_null=True)
    manufacturer = serializers.CharField(
        source="manufacturer.name", allow_null=True
    )
    service = serializers.CharField(
        source="service.name", allow_null=True
    )
    counter = serializers.SerializerMethodField(allow_null=True)

    def get_counter(self, obj: Vehicle) -> Optional[int]:
        try:
            return obj.counters.latest('date').value
        except Counter.DoesNotExist:
            return None

    class Meta:
        model = Vehicle
        fields = (
            'id',
            'avatar',
            'inventory_number',
            'manufacturer',
            'service',
            'brand',
            'year',
            'gov_number',
            'group',
            'counter',
        )


class VehicleDisplaySerializer(BaseSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleTypeSerializer(BaseSerializer):
    class Meta:
        model = VehicleType
        exclude = ('code',)


class ManufacturerSerializer(BaseSerializer):
    class Meta:
        model = Manufacturer
        exclude = ('code',)


class BrandSerializer(BaseSerializer):
    class Meta:
        model = Brand
        exclude = ('code',)


class VehicleBodySerializer(BaseSerializer):
    class Meta:
        model = VehicleBody
        exclude = ('code',)


class VehicleGroupSerializer(BaseSerializer):
    class Meta:
        model = VehicleGroup
        exclude = ('code',)


class FuelTypeSerializer(BaseSerializer):
    class Meta:
        model = FuelType
        exclude = ('code',)


class VehicleClassSerializer(BaseSerializer):
    class Meta:
        model = VehicleClass
        exclude = ('code',)


class ColorSerializer(BaseSerializer):
    class Meta:
        model = Color
        exclude = ('code',)


class MaintenanceServiceSerializer(BaseSerializer):
    class Meta:
        model = MaintenanceService
        exclude = ('code',)


class SubdivisionSerializer(BaseSerializer):
    class Meta:
        model = Subdivision
        exclude = ('code',)


class SourceSerializer(BaseSerializer):
    class Meta:
        model = Source
        exclude = ('code',)


class WarehouseSerializer(BaseSerializer):
    class Meta:
        model = Warehouse
        exclude = ('code',)


class HistorySerializer(serializers.ModelSerializer):
    content_type = serializers.CharField(source='content_type.model')
    verbose_name = serializers.SerializerMethodField()
    created_at = serializers.DateField(format="%Y-%m-%d", allow_null=True)

    def get_verbose_name(self, obj):
        model = obj.content_object._meta.model
        return str(model._meta.get_field(obj.field).verbose_name)

    class Meta:
        model = History
        fields = (
            'verbose_name',
            'content_type',
            'field',
            'value',
            'created_at'
        )


class CounterSerializer(BaseSerializer):
    vehicle = VehicleListSerializer(read_only=True)
    vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset=Vehicle.objects.all(), source='vehicle'
    )
    type = serializers.SerializerMethodField()
    date = serializers.DateTimeField(format="%Y-%m-%d")

    def get_type(self, obj):
        if hasattr(obj, "fueling"):
            return "fueling"
        elif hasattr(obj, "issue"):
            return "issue"
        return "manual"

    class Meta:
        model = Counter
        fields = '__all__'


class ExpenseTypeSerializer(BaseSerializer):
    class Meta:
        model = ExpenseType
        fields = "__all__"


class ExpenseSerializer(BaseSerializer):
    vehicle = VehicleListSerializer(read_only=True)
    vehicle_id = serializers.PrimaryKeyRelatedField(
        queryset=Vehicle.objects.all(), source='vehicle'
    )
    date = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseListSerializer(ExpenseSerializer):
    type = serializers.CharField(source='type.name', allow_null=True)

    class Meta:
        model = Expense
        fields = '__all__'
