from django.db import models


class Waybill(models.Model):
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

    def __str__(self) -> str:
        return f"{self.number} {self.date}"

    class Meta:
        verbose_name = "Накладная"
        verbose_name_plural = "Накладные"
