from django.db import models
from django.core.validators import MaxValueValidator


class Subdivision(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(
        max_length=35,
        null=True,
        default=None,
        verbose_name="Название Подразделения"
    )
    phone = models.CharField(
        max_length=10,
        null=True,
        default=None,
        verbose_name="Телефон"
    )
    chief = models.CharField(
        max_length=35,
        null=True,
        default=None,
        verbose_name="Начальник Подразделения"
    )
    percent_city = models.IntegerField(
        validators=[MaxValueValidator(99)],
        null=True,
        default=None,
        verbose_name="Процент города"
    )
    parent = models.ForeignKey(
        "self",
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = "Подразделение-владелец транспорта"
        verbose_name_plural = "Подразделения-владельцы транспорта"
