from django.db import models

from common.models import BaseModel, UserModel
from vehicles.models import Counter
from vehicles.models.vehicle import Vehicle


class ServiceTask(BaseModel):
    name = models.CharField(max_length=128)


class ServiceRecord(BaseModel):
    vechicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="service_records",
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    tasks = models.ManyToManyField(ServiceTask, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
    counter = models.OneToOneField(
        Counter,
        on_delete=models.CASCADE,
        related_name="records"
    )


class ServiceIssue(BaseModel):
    STATUSES = (
        ('open', 'open'),
        ('overdue', 'overdue'),
        ('solved', 'solved'),
        ('closed', 'closed'),
    )
    vechicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="issues"
    )
    summary = models.CharField(max_length=128)
    date = models.DateTimeField()
    due_date = models.DateTimeField()
    users = models.ManyToManyField(
        UserModel,
        verbose_name="Ответственные Лица",
        related_name='service_issues',
        blank=True
    )
    description = models.TextField()
    status = models.CharField(
        choices=STATUSES,
        max_length=10,
        blank=True,
        default='open'
    )
    service_record = models.ForeignKey(
        ServiceRecord,
        on_delete=models.CASCADE,
        null=True,
        default=None,
        blank=True
    )
    counter = models.OneToOneField(
        Counter,
        on_delete=models.CASCADE,
        related_name="issue"
    )