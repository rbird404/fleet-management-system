from django.db import models

from common.models import BaseModel
from vehicles.models.vehicle import Vehicle


class ExpenseType(BaseModel):
    name = models.CharField(max_length=128)


class Expense(BaseModel):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="expenses",
        verbose_name="ТС"
    )
    description = models.TextField(verbose_name="Описание причины расхода")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    type = models.ForeignKey(
        ExpenseType,
        on_delete=models.DO_NOTHING,
        verbose_name="Тип расходов"
    )
    reported_date = models.DateTimeField()
    # photos | files
