from django.db import models
from django.core.validators import MaxValueValidator


class Subdivision(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(
        verbose_name="Название Подразделения",
        max_length=35,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        verbose_name="Телефон",
        max_length=10,
        null=True,
        blank=True,
    )
    chief = models.CharField(
        verbose_name="Начальник Подразделения",
        max_length=35,
        null=True,
        blank=True,
    )
    percent_city = models.IntegerField(
        verbose_name="Процент города",
        validators=[MaxValueValidator(99)],
        null=True,
        blank=True,
    )
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = "Подразделение-владелец транспорта"
        verbose_name_plural = "Подразделения-владельцы транспорта"
