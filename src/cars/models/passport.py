from django.db import models

from cars.models.base import BaseModel


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

    def __str__(self) -> str:
        return f"{self.number} {self.date}"

    class Meta:
        verbose_name = "Тех. паспорт"
        verbose_name_plural = "Тех. паспорта"
