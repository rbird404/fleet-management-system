from django.db import models


class Distribution(models.Model):
    number = models.CharField(
        verbose_name="Номер распределения",
        max_length=15,
        null=True,
        default=None
    )
    date = models.DateField(
        verbose_name="Дата распределения",
        null=True,
        default=None
    )

    def __str__(self) -> str:
        return f"{self.number} {self.date}"

    class Meta:
        verbose_name = "Распределение"
        verbose_name_plural = "Распределения"
