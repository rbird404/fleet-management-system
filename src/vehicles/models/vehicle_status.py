from django.db import models
from .base import BaseModel


class VehicleStatus(BaseModel):
    name = models.CharField(max_length=32)
    color = models.CharField(max_length=8, null=True, blank=True)
