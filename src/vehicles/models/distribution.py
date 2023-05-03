from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


from common.models import BaseModel
from history.models import History


class Distribution(BaseModel):
    number = models.CharField(
        verbose_name="Номер распределения",
        max_length=15,
        null=True,
        blank=True,
    )
    date = models.DateField(
        verbose_name="Дата распределения",
        null=True,
        blank=True,
    )
    history = GenericRelation(History, related_query_name="distribution")

    def __str__(self) -> str:
        return f"{self.number} {self.date}"

    class Meta:
        verbose_name = "Распределение"
        verbose_name_plural = "Распределения"
