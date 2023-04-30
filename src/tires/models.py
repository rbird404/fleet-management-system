from django.db import models


class TireBrand(models.Model):
    name = models.CharField(max_length=16, unique=True)
    comment = models.TextField(blank=True)

    # производитель

    class Meta:
        verbose_name = 'Модель шины'
        verbose_name_plural = 'Модели шин'


class TireType(models.Model):
    name = models.CharField(max_length=16)

    class Meta:
        verbose_name = 'Тип шин'
        verbose_name_plural = 'Типы шин'


class TireSize(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'Размер шины'
        verbose_name_plural = 'Размеры шин'


class Seasonality(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'Сезонность'


class Tire(models.Model):
    # склад шин

    brand = models.ForeignKey(
        TireBrand,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Модель'
    )
    type = models.ForeignKey(
        TireType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Тип'
    )
    seasonality = models.ForeignKey(
        Seasonality,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Сезонность"
    )
    price = models.FloatField(
        verbose_name="Цена",
        null=True,
        blank=True
    )
    recommended_pressure = models.DecimalField(
        verbose_name="Рекомендованное постоянное давление",
        null=True,
        blank=True
    )
    is_spare = models.BooleanField(
        verbose_name="Запаска",
        default=False,
        blank=True
    )
    initial_mileage = models.DecimalField(
        verbose_name="Пробег с начала эксплуатации, км."
    )
    mileage_rate = models.IntegerField(
        verbose_name="Норма пробега, км."
    )
    receipt_date = models.DateTimeField(
        verbose_name="Дата поступления"
    )
    thread_depth = models.DecimalField(
        verbose_name="Рекомендованное давление"
    )
    comment = models.TextField(blank=True, null=True)


