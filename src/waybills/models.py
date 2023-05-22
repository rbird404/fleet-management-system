from django.db import models

from common.models import BaseModel
from vehicles.models import Vehicle


class Waybill(BaseModel):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        verbose_name="ТС"
    )
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


class Image(BaseModel):
    waybill = models.ManyToManyField(
        Waybill,
        blank=True,
        related_name='images',
        verbose_name="Накладные"
    )
    image = models.ImageField(upload_to='images/waybills/')

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class File(BaseModel):
    waybill = models.ManyToManyField(
        Waybill,
        blank=True,
        related_name='files',
        verbose_name="Накладные"
    )
    file = models.FileField(upload_to='files/waybills/')

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"