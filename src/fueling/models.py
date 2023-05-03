from django.db import models

from common.models import BaseModel
from vehicles.models.vehicle_items import FuelType
from vehicles.models.vehicle import Vehicle
from vehicles.models.counter import Counter


class Fueling(BaseModel):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="fueling"
    )
    counter = models.OneToOneField(
        Counter,
        on_delete=models.CASCADE,
        related_name="fueling"
    )
    fuel_type = models.ForeignKey(
        FuelType,
        verbose_name="Марка бензина",
        on_delete=models.SET_NULL,
        null=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    summ = models.DecimalField(max_digits=10, decimal_places=2)
    liters = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    # photos | files
