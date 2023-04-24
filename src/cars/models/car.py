from django.db import models
from django.core.validators import MaxValueValidator

from cars.models.distribution import Distribution
from cars.models.engine import Engine
from cars.models.passport import Passport
from cars.models.subdivision import Subdivision
from cars.models.waybill import Waybill
from cars.models.car_items import (
    CarBody, CarClass, CarGroup, CarType, Brand, Warehouse,
    Manufacturer, MaintenanceService, Color, Source, GasolineBrand
)


class Car(models.Model):
    CATEGORIES = (
        ("a", 'A'),
        ("b", 'B'),
        ("c", 'C'),
        ("d", 'D'),
    )

    inventory_number = models.PositiveIntegerField(
        verbose_name="Инвентарный номер",
        validators=[MaxValueValidator(99999)],
        unique=True
    )
    type = models.ForeignKey(
        CarType,
        verbose_name="Тип транспорта",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        verbose_name="Завод-Изготовитель",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    brand = models.ForeignKey(
        Brand,
        verbose_name="Марка",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    body = models.ForeignKey(
        CarBody,
        verbose_name="Тип Кузова",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    group = models.ForeignKey(
        CarGroup,
        verbose_name="Штатная группа",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    chass_number = models.CharField(
        verbose_name="Номер Шасси",
        max_length=8,
        null=True,
        default=None
    )
    body_number = models.CharField(
        verbose_name="Номер Кузова",
        null=True,
        default=None,
        max_length=8
    )
    year = models.PositiveIntegerField(
        verbose_name="Год выпуска",
        validators=[MaxValueValidator(9999)],
        null=True,
        default=None,
    )
    passport = models.OneToOneField(
        Passport,
        verbose_name="Тех. паспорт",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    gov_number = models.CharField(
        verbose_name="Номер государственной регистрации",
        max_length=16,
        null=True,
        default=None
    )
    register_number = models.CharField(
        verbose_name="Реестровый номер",
        max_length=16,
        null=True,
        default=None
    )
    sign_date = models.DateField(
        verbose_name="Дата выдачи номерного знака",
        null=True,
        default=None
    )
    exploitation_date = models.DateField(
        verbose_name="Дата ввода в эксплутацию",
        null=True,
        default=None,
    )
    car_class = models.ForeignKey(
        CarClass,
        db_column='class',
        verbose_name="Класс автомобиля",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    color = models.ForeignKey(
        Color,
        verbose_name="Цвет автомобиля",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    service = models.ForeignKey(
        MaintenanceService,
        verbose_name="Служба эксплутации",
        on_delete=models.SET_NULL,
        null=True,
        default=None,
    )
    subdivision = models.ForeignKey(
        Subdivision,
        db_column='owner',
        verbose_name="Подразделение-владелец транспорта",
        on_delete=models.SET_NULL,
        null=True,
        default=None,
    )
    cost = models.DecimalField(
        verbose_name="Балансовая стоимость",
        max_digits=18,
        decimal_places=2,
        null=True,
        default=None,
    )
    source = models.ForeignKey(
        Source,
        verbose_name="Источник получения",
        on_delete=models.SET_NULL,
        null=True,
        default=None,
    )
    source_number = models.CharField(
        verbose_name="Номер Фондового извещения",
        max_length=16,
        null=True,
        default=None
    )
    source_date = models.DateField(
        verbose_name="Дата документа",
        null=True,
        default=None
    )
    warehouse = models.ForeignKey(
        Warehouse,
        verbose_name="Склад",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    waybill = models.OneToOneField(
        Waybill,
        verbose_name="Накладная",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    distribution = models.OneToOneField(
        Distribution,
        verbose_name="Распределение",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    transfer_date = models.DateField(
        verbose_name="Дата передачи в подразделение",
        null=True,
        default=None
    )
    del_date = models.DateField(
        verbose_name="Дата списания",
        null=True,
        default=None
    )
    mileage_rate = models.DecimalField(
        verbose_name="Месячная норма пробега",
        max_digits=8,
        decimal_places=2,
        null=True,
        default=None
    )
    fuel_rate = models.DecimalField(
        verbose_name="Норма расхода топлива на 100 км",
        max_digits=6,
        decimal_places=2,
        null=True,
        default=None
    )
    id_number = models.CharField(
        verbose_name="Идентификационный номер",
        max_length=20,
        null=True,
        default=None
    )
    gasoline_brand = models.ForeignKey(
        GasolineBrand,
        verbose_name="Марка бензина",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    engine = models.OneToOneField(
        Engine,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        verbose_name="Двигатель Т/С"
    )
    climate_control = models.BooleanField(
        verbose_name="Наличие системы Климат контроль",
        null=True,
        default=None,
    )
    base_rate = models.DecimalField(
        verbose_name="Базовая норма расхода топлива",
        max_digits=6,
        decimal_places=2,
        null=True,
        default=None,
    )
    identifier_fuel_rate = models.IntegerField(
        verbose_name="Инд. процент баз. нормы расхода топлива",
        validators=[MaxValueValidator(999)],
        null=True,
        default=None,
    )
    category = models.CharField(
        choices=CATEGORIES,
        verbose_name="Категория автомобиля",
        max_length=1,
        null=True,
        default=None
    )
    trust_date = models.DateField(
        verbose_name="Дата действия страхавого полиса",
        null=True,
        blank=True
    )
    to_date = models.DateField(
        verbose_name="Дата действия технического осмотра",
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name="Дата ввода", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления", auto_now=True
    )

    def __str__(self):
        return f"Auto#{self.id} inv#{self.inventory_number}"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
