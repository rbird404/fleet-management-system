from django.db import models

from common.models import BaseModel
from vehicles.models import Vehicle, FuelType, Counter


class Fueling(BaseModel):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="fueling",
        verbose_name="ТС"
    )
    counter = models.OneToOneField(
        Counter,
        on_delete=models.CASCADE,
        related_name="fueling",
        verbose_name="Счетчик"
    )
    fuel_type = models.ForeignKey(
        FuelType,
        verbose_name="Марка бензина",
        on_delete=models.SET_NULL,
        null=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за литр")
    summ = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    liters = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Объем")
    date = models.DateTimeField(verbose_name="Дата")

    class Meta:
        verbose_name = "Заправка"
        verbose_name_plural = "Заправки"
