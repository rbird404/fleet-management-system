from django.db import models

from common.models import BaseModel
from vehicles.models.vehicle import Vehicle


class Counter(BaseModel):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="counters",
        verbose_name="ТС"
    )
    date = models.DateTimeField(verbose_name="Дата")
    value = models.IntegerField(verbose_name="Показания счетчика")

    class Meta:
        verbose_name = "Счетчик"
        verbose_name_plural = "Счетчики"
