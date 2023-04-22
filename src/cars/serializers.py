from collections import OrderedDict
from rest_framework import serializers
from django.db import models
from cars.models import (
    CarType, CarBody, CarClass, CarGroup, Color, Manufacturer, Brand, Source,
    MaintenanceService, Warehouse, Waybill, GasolineBrand, Subdivision, Engine,
    Passport, Distribution, Car
)


class CarTypeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = CarType
        exclude = ('code',)


class ManufacturerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Manufacturer
        exclude = ('code',)


class BrandSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Brand
        exclude = ('code',)


class CarBodySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = CarBody
        exclude = ('code',)


class CarGroupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = CarGroup
        exclude = ('code',)


class GasolineBrandSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = GasolineBrand
        exclude = ('code',)


class CarClassSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = CarClass
        exclude = ('code',)


class ColorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Color
        exclude = ('code',)


class MaintenanceServiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = MaintenanceService
        exclude = ('code',)


class SubdivisionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Subdivision
        exclude = ('code',)


class SourceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Source
        exclude = ('code',)


class WarehouseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Warehouse
        exclude = ('code',)


class EngineSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Engine
        fields = '__all__'


class WaybillSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Waybill
        fields = '__all__'


class DistributionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Distribution
        fields = '__all__'


class PassportSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Passport
        fields = '__all__'


class CarDetailSerializer(serializers.ModelSerializer):
    engine = EngineSerializer(
        required=False, allow_null=True
    )
    type = CarTypeSerializer(
        required=False, allow_null=True
    )
    manufacturer = ManufacturerSerializer(
        required=False, allow_null=True
    )
    brand = BrandSerializer(
        required=False, allow_null=True
    )
    body = CarBodySerializer(
        required=False, allow_null=True
    )
    group = CarGroupSerializer(
        required=False, allow_null=True
    )
    passport = PassportSerializer(
        required=False, allow_null=True
    )
    color = ColorSerializer(
        required=False, allow_null=True
    )
    service = MaintenanceServiceSerializer(
        required=False, allow_null=True)
    subdivision = SubdivisionSerializer(
        required=False, allow_null=True
    )
    source = SourceSerializer(
        required=False, allow_null=True
    )
    warehouse = WarehouseSerializer(
        required=False, allow_null=True
    )
    distribution = DistributionSerializer(
        required=False, allow_null=True
    )
    gasoline_brand = GasolineBrandSerializer(
        required=False, allow_null=True, default=None
    )
    waybill = WaybillSerializer(
        required=False, allow_null=True
    )
    car_class = CarClassSerializer(
        required=False, allow_null=True
    )

    def _get_or_create(
        self, model: models.Model, data: dict | None
    ) -> models.Model | None:
        if data is None:
            return None

        id_ = data.get("id")
        if id_ is not None:
            try:
                return model.objects.get(id=id_)
            except model.DoesNotExist:
                raise serializers.ValidationError(
                    f"{model.__name__}  {id_} doesn't exist"
                )

        return model.objects.create(**data)

    def create(self, validated_data: dict):
        nested_fields = {}

        for field, value in validated_data.items():
            if isinstance(value, OrderedDict):
                nested_fields[field] = self._get_or_create(
                    self.fields[field].Meta.model, value
                )

        validated_data.update(nested_fields)

        return super().create(validated_data)

    class Meta:
        model = Car
        fields = '__all__'
