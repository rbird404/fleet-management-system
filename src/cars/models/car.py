from django.db import models
from django.core.validators import MaxValueValidator

from cars.models.base import BaseModel
from cars.models.distribution import Distribution
from cars.models.engine import Engine
from cars.models.passport import Passport
from cars.models.subdivision import Subdivision
from cars.models.waybill import Waybill
from cars.models.car_items import (
    CarBody, CarClass, CarGroup, CarType, Brand, Warehouse,
    Manufacturer, MaintenanceService, Color, Source, GasolineBrand
)


class Car(BaseModel):
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
        blank=True,
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        verbose_name="Завод-Изготовитель",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    brand = models.ForeignKey(
        Brand,
        verbose_name="Марка",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    body = models.ForeignKey(
        CarBody,
        verbose_name="Тип Кузова",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    group = models.ForeignKey(
        CarGroup,
        verbose_name="Штатная группа",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    chass_number = models.CharField(
        verbose_name="Номер Шасси",
        max_length=8,
        null=True,
        blank=True,
    )
    body_number = models.CharField(
        verbose_name="Номер Кузова",
        null=True,
        blank=True,
        max_length=8
    )
    year = models.PositiveIntegerField(
        verbose_name="Год выпуска",
        validators=[MaxValueValidator(9999)],
        null=True,
        blank=True
    )
    passport = models.OneToOneField(
        Passport,
        verbose_name="Тех. паспорт",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    gov_number = models.CharField(
        verbose_name="Номер государственной регистрации",
        max_length=16,
        null=True,
        blank=True,
    )
    register_number = models.CharField(
        verbose_name="Реестровый номер",
        max_length=16,
        null=True,
        blank=True,
    )
    sign_date = models.DateField(
        verbose_name="Дата выдачи номерного знака",
        null=True,
        blank=True,
    )
    exploitation_date = models.DateField(
        verbose_name="Дата ввода в эксплутацию",
        null=True,
        blank=True
    )
    car_class = models.ForeignKey(
        CarClass,
        db_column='class',
        verbose_name="Класс автомобиля",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    color = models.ForeignKey(
        Color,
        verbose_name="Цвет автомобиля",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    service = models.ForeignKey(
        MaintenanceService,
        verbose_name="Служба эксплутации",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    subdivision = models.ForeignKey(
        Subdivision,
        db_column='owner',
        verbose_name="Подразделение-владелец транспорта",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    cost = models.DecimalField(
        verbose_name="Балансовая стоимость",
        max_digits=18,
        decimal_places=2,
        null=True,
        blank=True
    )
    source = models.ForeignKey(
        Source,
        verbose_name="Источник получения",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    source_number = models.CharField(
        verbose_name="Номер Фондового извещения",
        max_length=16,
        null=True,
        blank=True,
    )
    source_date = models.DateField(
        verbose_name="Дата документа",
        null=True,
        blank=True,
    )
    warehouse = models.ForeignKey(
        Warehouse,
        verbose_name="Склад",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    waybill = models.OneToOneField(
        Waybill,
        verbose_name="Накладная",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    distribution = models.OneToOneField(
        Distribution,
        verbose_name="Распределение",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    transfer_date = models.DateField(
        verbose_name="Дата передачи в подразделение",
        null=True,
        blank=True,
    )
    del_date = models.DateField(
        verbose_name="Дата списания",
        null=True,
        blank=True,
    )
    mileage_rate = models.DecimalField(
        verbose_name="Месячная норма пробега",
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
    )
    fuel_rate = models.DecimalField(
        verbose_name="Норма расхода топлива на 100 км",
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )
    id_number = models.CharField(
        verbose_name="Идентификационный номер",
        max_length=20,
        null=True,
        blank=True,
    )
    gasoline_brand = models.ForeignKey(
        GasolineBrand,
        verbose_name="Марка бензина",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    engine = models.OneToOneField(
        Engine,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Двигатель Т/С"
    )
    climate_control = models.BooleanField(
        verbose_name="Наличие системы Климат контроль",
        null=True,
        blank=True
    )
    base_rate = models.DecimalField(
        verbose_name="Базовая норма расхода топлива",
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    identifier_fuel_rate = models.IntegerField(
        verbose_name="Инд. процент баз. нормы расхода топлива",
        validators=[MaxValueValidator(999)],
        null=True,
        blank=True
    )
    category = models.CharField(
        verbose_name="Категория автомобиля",
        choices=CATEGORIES,
        max_length=1,
        null=True,
        blank=True,
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
