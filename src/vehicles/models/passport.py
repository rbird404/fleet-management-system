from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from common.models import BaseModel
from history.models import History


class Passport(BaseModel):
    number = models.CharField(
        verbose_name="Номер тех. паспорта",
        max_length=10,
        null=True,
        blank=True
    )
    date = models.DateField(
        verbose_name="Дата выдачи тех. паспорта",
        null=True,
        blank=True
    )
    history = GenericRelation(History, related_query_name="passport")

    def __str__(self) -> str:
        return f"{self.number} {self.date}"

    class Meta:
        verbose_name = "Тех. паспорт"
        verbose_name_plural = "Тех. паспорта"
