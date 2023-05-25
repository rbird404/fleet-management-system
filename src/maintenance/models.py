from django.db import models

from common.models import BaseModel, UserModel
from vehicles.models import Vehicle, Counter


class Task(BaseModel):
    order = models.IntegerField(
        blank=True, null=True,
        default=None, verbose_name="Порядковый номер"
    )
    name = models.CharField(max_length=128, verbose_name="Название")

    class Meta:
        verbose_name = "Сервисная задача"
        verbose_name_plural = "Сервисные задачи"


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
        related_name="service_issues",
        verbose_name="ТС"
    )
    summary = models.CharField(max_length=128, verbose_name="Проблема")
    date = models.DateTimeField(verbose_name="Дата")
    due_date = models.DateTimeField(verbose_name="Крайний срок")
    users = models.ManyToManyField(
        UserModel,
        verbose_name="Ответственные лица",
        related_name='service_issues',
        blank=True
    )
    description = models.TextField(
        blank=True,
        null=True,
        default=None,
        verbose_name="Описание"
    )
    status = models.CharField(
        choices=STATUSES,
        max_length=10,
        blank=True,
        default='open',
        verbose_name="Статус"
    )
    counter = models.OneToOneField(
        Counter,
        on_delete=models.CASCADE,
        related_name="issue",
        verbose_name="Счетчик"
    )

    class Meta:
        verbose_name = "Проблема"
        verbose_name_plural = "Проблемы"


class Record(BaseModel):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name="service_records",
        verbose_name="ТС"
    )
    start_date = models.DateTimeField(
        blank=True, null=True,
        default=None,
        verbose_name="Дата начала"
    )
    end_date = models.DateTimeField(
        blank=True, null=True,
        default=None, verbose_name="Дата окончания"
    )
    tasks = models.ManyToManyField(
        Task,
        blank=True,
        verbose_name="Задачи"
    )
    issues = models.ManyToManyField(
        Issue,
        blank=True,
        verbose_name="Проблемы"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Цена"
    )
    counter = models.OneToOneField(
        Counter,
        on_delete=models.CASCADE,
        related_name="record",
        verbose_name="Счетчик"
    )

    class Meta:
        verbose_name = "Сервисная запись"
        verbose_name_plural = "Сервисные записи"
