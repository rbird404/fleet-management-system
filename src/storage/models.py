from django.db import models
from common.models import BaseModel
from waybills.models import Waybill
from fueling.models import Fueling
from vehicle_service.models import ServiceIssue, ServiceRecord, ServiceTask
from vehicles.models import Vehicle
from expenses.models import Expense
from vehicles.models.subdivision import Subdivision
from vehicles.models.vehicle_items import (
    Warehouse, Manufacturer, MaintenanceService, Source
)


class Image(BaseModel):
    image = models.ImageField(upload_to='images')
    vehicle = models.ManyToManyField(
        Vehicle,
        blank=True,
        related_name="images"
    )
    subdivisions = models.ManyToManyField(
        Subdivision,
        blank=True,
        related_name="images"
    )
    warehouses = models.ManyToManyField(
        Warehouse,
        blank=True,
        related_name="images"
    )
    manufacturer = models.ManyToManyField(
        Manufacturer,
        blank=True,
        related_name="images"
    )
    maintenanceService = models.ManyToManyField(
        MaintenanceService,
        blank=True,
        related_name="images"
    )
    source = models.ManyToManyField(
        Source,
        blank=True,
        related_name="images"
    )
    issues = models.ManyToManyField(
        ServiceIssue,
        blank=True,
        related_name="images"
    )
    records = models.ManyToManyField(
        ServiceRecord,
        blank=True,
        related_name="images"
    )
    tasks = models.ManyToManyField(
        ServiceTask,
        blank=True,
        related_name="images"
    )
    waybills = models.ManyToManyField(
        Waybill,
        blank=True,
        related_name="images"
    )
    fueling = models.ManyToManyField(
        Fueling,
        blank=True,
        related_name="images"
    )
    expenses = models.ManyToManyField(
        Expense,
        blank=True,
        related_name="images"
    )


class File(BaseModel):
    file = models.FileField(upload_to='files')
    vehicle = models.ManyToManyField(
        Vehicle,
        blank=True,
        related_name="files"
    )
    subdivisions = models.ManyToManyField(
        Subdivision,
        blank=True,
        related_name="files"
    )
    warehouses = models.ManyToManyField(
        Warehouse,
        blank=True,
        related_name="files"
    )
    manufacturer = models.ManyToManyField(
        Manufacturer,
        blank=True,
        related_name="files"
    )
    maintenanceService = models.ManyToManyField(
        MaintenanceService,
        blank=True,
        related_name="files"
    )
    source = models.ManyToManyField(
        Source,
        blank=True,
        related_name="files"
    )
    issues = models.ManyToManyField(
        ServiceIssue,
        blank=True,
        related_name="files"
    )
    records = models.ManyToManyField(
        ServiceRecord,
        blank=True,
        related_name="files"
    )
    tasks = models.ManyToManyField(
        ServiceTask,
        blank=True,
        related_name="files"
    )
    waybills = models.ManyToManyField(
        Waybill,
        blank=True,
        related_name="files"
    )
    fueling = models.ManyToManyField(
        Fueling,
        blank=True,
        related_name="files"
    )
    expenses = models.ManyToManyField(
        Expense,
        blank=True,
        related_name="files"
    )
