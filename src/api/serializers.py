from collections import OrderedDict
from rest_framework import serializers
from cars.models import (
    Waybill, Engine, Passport, Distribution, Car,
    CarType, Brand, Manufacturer, CarBody, CarGroup,
    CarClass, GasolineBrand, Color, MaintenanceService,
    Subdivision, Source, Warehouse
)


class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        exclude = ('is_deleted',)


class WaybillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waybill
        exclude = ('is_deleted',)


class DistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribution
        exclude = ('is_deleted',)


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        exclude = ('is_deleted',)


class CarCreateUpdateSerializer(serializers.ModelSerializer):
    engine = EngineSerializer()
    distribution = DistributionSerializer()
    passport = PassportSerializer()
    waybill = WaybillSerializer()

    def create(self, validated_data: OrderedDict) -> Car:
        nested_fields = {}
        for field, data in validated_data.items():
            if isinstance(data, OrderedDict):
                nested_fields[field] = (
                    self.fields[field].Meta.model.objects.create(**data)
                )
        validated_data.update(nested_fields)
        return super().create(validated_data)

    def update(self, instance: Car, validated_data: OrderedDict) -> Car:
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
        model = Car
        exclude = ('is_deleted',)


class CarListSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source="brand.name", allow_null=True)
    group = serializers.CharField(source='group.name', allow_null=True)

    class Meta:
        model = Car
        fields = (
            'id',
            'inventory_number',
            'brand',
            'year',
            'gov_number',
            'group'
        )


class CarDisplaySerializer(CarCreateUpdateSerializer, CarListSerializer):
    type = serializers.CharField(
        source='type.name', allow_null=True
    )
    manufacturer = serializers.CharField(
        source='manufacturer.name', allow_null=True
    )
    body = serializers.CharField(
        source="body.name", allow_null=True
    )
    car_class = serializers.CharField(
        source="car_class.name", allow_null=True
    )
    color = serializers.CharField(
        source="color.name", allow_null=True
    )
    service = serializers.CharField(
        source="service.name", allow_null=True
    )
    subdivision = serializers.CharField(
        source="subdivision.name", allow_null=True
    )
    source = serializers.CharField(
        source="source.name", allow_null=True
    )
    warehouse = serializers.CharField(
        source="warehouse.name", allow_null=True
    )
    gasoline_brand = serializers.CharField(
        source="gasoline_brand.name", allow_null=True
    )

    class Meta:
        model = Car
        exclude = ('is_deleted',)


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        exclude = ('code', 'is_deleted')


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        exclude = ('code', 'is_deleted')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ('code', 'is_deleted')


class CarBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBody
        exclude = ('code', 'is_deleted')


class CarGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGroup
        exclude = ('code', 'is_deleted')


class GasolineBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasolineBrand
        exclude = ('code', 'is_deleted')


class CarClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarClass
        exclude = ('code', 'is_deleted')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        exclude = ('code', 'is_deleted')


class MaintenanceServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceService
        exclude = ('code', 'is_deleted')


class SubdivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdivision
        exclude = ('code', 'is_deleted')


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        exclude = ('code', 'is_deleted')


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        exclude = ('code', 'is_deleted')
