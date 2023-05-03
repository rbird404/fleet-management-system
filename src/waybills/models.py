from django.db import models

from common.models import BaseModel
from vehicles.models.vehicle import Vehicle


class Waybill(BaseModel):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
    )
    number = models.CharField(
        verbose_name="Номер накладной",
        max_length=128
    )
    date = models.DateField(
        verbose_name="Дата накладной",
        null=True,
        auto_now_add=True
    )

    def __str__(self) -> str:
        return f"{self.number} {self.date}"

    class Meta:
        verbose_name = "Накладная"
        verbose_name_plural = "Накладные"
