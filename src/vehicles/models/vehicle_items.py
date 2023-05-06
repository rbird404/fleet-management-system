from django.db import models

from common.models import BaseModel


class VehicleItemBase(BaseModel):
    name = models.CharField(max_length=40, null=True)
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        abstract = True


class VehicleType(VehicleItemBase):
    class Meta:
        verbose_name = "Тип транспортного средства"
        verbose_name_plural = "Типы Транспортных средств"


class Manufacturer(VehicleItemBase):
    class Meta:
        verbose_name = "Завод Изготовитель"
        verbose_name_plural = "Заводы Изготовителя"


class Brand(VehicleItemBase):
    class Meta:
        verbose_name = "Марка транспортного средства"
        verbose_name_plural = "Марки Транспортных средств"


class VehicleBody(VehicleItemBase):
    class Meta:
        verbose_name = "Тип Кузова"
        verbose_name_plural = "Тип Кузовов"


class VehicleGroup(VehicleItemBase):
    class Meta:
        verbose_name = "Штатная группа"
        verbose_name_plural = "Штатные группы"


class FuelType(VehicleItemBase):
    class Meta:
        verbose_name = "Вид топлива"
        verbose_name_plural = "Виды топлива"


class VehicleClass(VehicleItemBase):
    class Meta:
        verbose_name = "Класс Автотранспорта"
        verbose_name_plural = "Классы Автотранспорта"


class Color(VehicleItemBase):
    class Meta:
        verbose_name = "Цвет Автотранспорта"
        verbose_name_plural = "Цвета Автотранспорта"


class MaintenanceService(VehicleItemBase):
    class Meta:
        verbose_name = "Служба эксплуатации автомобиля"
        verbose_name_plural = "Службы эксплутации автомобиля"


class Source(VehicleItemBase):
    class Meta:
        verbose_name = "Организ., выдавшая наряд"
        verbose_name_plural = "Организ., выдавшая наряд"


class Warehouse(VehicleItemBase):
    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"
