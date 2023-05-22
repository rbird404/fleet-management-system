from django.db import models

from common.models import BaseModel
from vehicles.models.vehicle import Vehicle


class VehicleImage(BaseModel):
    vehicle = models.ManyToManyField(
        Vehicle,
        blank=True,
        related_name='images',
        verbose_name="ТС"
    )
    image = models.ImageField(upload_to='images/vehicles/', verbose_name="Фото")

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class VehicleFile(BaseModel):
    vehicle = models.ManyToManyField(
        Vehicle,
        blank=True,
        related_name='files',
        verbose_name="ТС"
    )
    file = models.FileField(upload_to='files/vehicles/', verbose_name="Файл")

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
