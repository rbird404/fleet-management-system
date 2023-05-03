from django.db import models

from common.models import BaseModel
from vehicles.models.vehicle import Vehicle


class Counter(BaseModel):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="counters"
    )
    date = models.DateTimeField()
    value = models.IntegerField(verbose_name="Показания счетчика")
