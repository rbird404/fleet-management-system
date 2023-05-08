from rest_framework import serializers


class VehicleCountSerializer(serializers.Serializer):
    count = serializers.IntegerField()


class IssueCountSerializer(serializers.Serializer):
    open = serializers.IntegerField()
    overdue = serializers.IntegerField()


class TotalMileageSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    counter = serializers.IntegerField()


class VehicleTopCounterSerializer(serializers.Serializer):
    inv_number = serializers.IntegerField()
    counter = serializers.IntegerField()


class VehicleTopFuelingSerializer(serializers.Serializer):
    inv_number = serializers.IntegerField()
    price = serializers.DecimalField(decimal_places=2, max_digits=10)


class FuelCostSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    cost = serializers.DecimalField(decimal_places=2, max_digits=10)


class CostPerKilometerSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    price = serializers.DecimalField(decimal_places=2, max_digits=10)


class ExpensesCostSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    price = serializers.DecimalField(decimal_places=2, max_digits=10)


class ServiceCostSerializer(serializers.Serializer):
    month = serializers.IntegerField()
    price = serializers.DecimalField(decimal_places=2, max_digits=10)
