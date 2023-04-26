from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from datetime import date
from decimal import Decimal
from types import NoneType

TYPES = {
    int: 'int',
    date: 'date',
    bool: 'bool',
    Decimal: 'decimal',
    str: 'str',
    NoneType: 'none'
}


class History(models.Model):
    TYPES = (
        ('int', 'int'),
        ('date', 'date'),
        ('bool', 'bool'),
        ('decimal', 'decimal'),
        ('str', 'str'),
        ('none', 'none')
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    field = models.CharField(max_length=32)
    value = models.TextField(null=True, blank=True)
    value_type = models.CharField(choices=TYPES, max_length=8)
    created_at = models.DateField(
        verbose_name="Дата ввода", null=True
    )

    def __str__(self):
        return f"{self.content_type.name} {self.field} {self.created_at}"

    class Meta:
        verbose_name = "История изменений"
        verbose_name_plural = "История изменений"