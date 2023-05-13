from django.db import models
from common.models import BaseModel
from vehicles.models.vehicle import Vehicle


class VehicleImage(BaseModel):
    vehicle = models.ManyToManyField(
        Vehicle,
        blank=True,
        related_name='images'
    )
    image = models.ImageField(upload_to='images/vehicles/')


class VehicleFile(BaseModel):
    vehicle = models.ManyToManyField(
        Vehicle,
        blank=True,
        related_name='files'
    )
    file = models.FileField(upload_to='files/vehicles/')
