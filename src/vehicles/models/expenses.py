from django.db import models

from common.models import BaseModel
from vehicles.models.vehicle import Vehicle


class ExpenseType(BaseModel):
    name = models.CharField(max_length=128)


class Expense(BaseModel):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )
    description = models.TextField()
    type = models.ForeignKey(
        ExpenseType,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
