from django.db import models


class PartCategory(models.Model):
    name = models.CharField(max_length=16)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Unit(models.Model):
    name = models.CharField(max_length=16)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'


class PartStorage(models.Model):
    code = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=128,blank=True)
    description = models.TextField(blank=True)


class Part(models.Model):
    # производитель
    name = models.CharField(max_length=128, unique=True)
    price = models.DecimalField()
    planned_mileage = models.PositiveIntegerField(
        verbose_name='Плановая сходимость'
    )
    category = models.ForeignKey(
        PartCategory
    )
    unit = models.ForeignKey(
        Unit
    )
    storage = models.ForeignKey(
        PartStorage
    )
    description = models.TextField()