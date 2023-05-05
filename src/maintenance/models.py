from django.db import models
from common.models import BaseModel, UserModel
from vehicles.models import Vehicle, Counter


class Task(BaseModel):
    order = models.IntegerField(blank=True, null=True, default=None)
    name = models.CharField(max_length=128)


class Issue(BaseModel):
    STATUSES = (
        ('open', 'open'),
        ('overdue', 'overdue'),
        ('solved', 'solved'),
        ('closed', 'closed'),
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="service_issues"
    )
    summary = models.CharField(max_length=128)
    date = models.DateTimeField()
    due_date = models.DateTimeField()
    users = models.ManyToManyField(
        UserModel,
        verbose_name="Ответственные лица",
        related_name='service_issues',
        blank=True
    )
    description = models.TextField(
        blank=True,
        null=True,
        default=None
    )
    status = models.CharField(
        choices=STATUSES,
        max_length=10,
        blank=True,
        default='open'
    )
    counter = models.OneToOneField(
        Counter,
        on_delete=models.CASCADE,
        related_name="issue"
    )


class Record(BaseModel):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="service_records",
    )
    start_date = models.DateTimeField(blank=True, null=True, default=None)
    end_date = models.DateTimeField(blank=True, null=True, default=None)
    tasks = models.ManyToManyField(
        Task,
        blank=True
    )
    issues = models.ManyToManyField(
        Issue,
        blank=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        blank=True
    )
    counter = models.OneToOneField(
        Counter,
        on_delete=models.CASCADE,
        related_name="record"
    )
