from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from vehicles.models import Vehicle, Counter


class CounterValidator:
    requires_context = True

    def __init__(self, counter_value_field="value", vehicle_field="vehicle"):
        self.counter_value_field = counter_value_field
        self.vehicle_field = vehicle_field

    def __call__(self, attrs, serializer):
        vehicle: Vehicle = attrs.get(self.vehicle_field)
        value = attrs.get(self.counter_value_field)

        instance = serializer.instance

        if not instance:
            query = Counter.objects.filter(vehicle=vehicle)
            if query.exists():
                last_counter = query.latest("id")
                if last_counter.value > value:
                    raise serializers.ValidationError(
                        _("The counter value must not be"
                          f" less than {last_counter.value}")
                    )
        else:
            query = Counter.objects.filter(
                vehicle=vehicle
            ).exclude(pk=instance.pk)
            try:
                prev = query.filter(
                    date__lte=instance.date, pk__lt=instance.pk
                ).latest('date').value
                if value < prev:
                    raise serializers.ValidationError(
                        _(f"The counter value must be greater than {prev}")
                    )
            except Counter.DoesNotExist:
                pass
            try:
                next_ = query.filter(
                    date__lte=instance.date, pk__gt=instance.pk
                ).earliest('date').value
                if value > next_:
                    raise serializers.ValidationError(
                        _("The counter value must not be"
                          f" less than {next_}")
                    )
            except Counter.DoesNotExist:
                pass
