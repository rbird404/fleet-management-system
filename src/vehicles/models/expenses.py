from django.db import models

from common.models import BaseModel
from vehicles.models.vehicle import Vehicle


class ExpenseType(BaseModel):
    name = models.CharField(max_length=128, verbose_name="Название")

    class Meta:
        verbose_name = "Тип Доп. расхода"
        verbose_name_plural = "Типы Доп. расходов"


class Expense(BaseModel):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="expenses",
        verbose_name="ТС"
    )
    description = models.TextField(verbose_name="Описание")
    type = models.ForeignKey(
        ExpenseType,
        on_delete=models.CASCADE,
        verbose_name="Тип"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    date = models.DateTimeField(verbose_name="Дата")

    class Meta:
        verbose_name = "Доп. расход"
        verbose_name_plural = "Доп. расходы"
