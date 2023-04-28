from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


from cars.models.base import BaseModel
from history.models import History


class Waybill(BaseModel):
    number = models.CharField(
        verbose_name="Номер накладной",
        max_length=16,
        null=True,
        default=None
    )
    date = models.DateField(
        verbose_name="Дата накладной",
        null=True,
        default=None
    )
    history = GenericRelation(History, related_query_name="waybill")

    def __str__(self) -> str:
        return f"{self.number} {self.date}"

    class Meta:
        verbose_name = "Накладная"
        verbose_name_plural = "Накладные"
