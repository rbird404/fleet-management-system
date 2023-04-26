from django.db import models

from cars.models.base import BaseModel


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

    def __str__(self) -> str:
        return f"{self.number} {self.date}"

    class Meta:
        verbose_name = "Распределение"
        verbose_name_plural = "Распределения"
