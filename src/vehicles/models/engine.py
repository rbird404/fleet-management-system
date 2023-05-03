from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from common.models import BaseModel
from history.models import History


class Engine(BaseModel):
    number = models.CharField(
        verbose_name="Номер Двигателя",
        max_length=16,
        null=True,
        blank=True,
    )
    model = models.CharField(
        verbose_name="Модель двигателя т/c",
        max_length=15,
        null=True,
        blank=True,
    )
    power = models.IntegerField(
        verbose_name="Мощность двигателя т/c",
        null=True,
        blank=True,
    )
    capacity = models.DecimalField(
        verbose_name="Объем двигателя т/с",
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )
    history = GenericRelation(History, related_query_name="engine")

    def __str__(self) -> str:
        return f"{self.number} {self.model}"

    class Meta:
        verbose_name = "Двигатель Т/C"
        verbose_name_plural = "Двигатели Т/C"
