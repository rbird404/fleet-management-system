from django.db import models


class CarItemBase(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True


class CarType(CarItemBase):
    class Meta:
        verbose_name = "Тип транспортного средства"
        verbose_name_plural = "Типы Транспортных средств"


class Manufacturer(CarItemBase):
    class Meta:
        verbose_name = "Завод Изготовитель"
        verbose_name_plural = "Заводы Изготовителя"


class Brand(CarItemBase):
    class Meta:
        verbose_name = "Марка транспортного средства"
        verbose_name_plural = "Марки Транспортных средств"


class CarBody(CarItemBase):
    class Meta:
        verbose_name = "Тип Кузова"
        verbose_name_plural = "Тип Кузовов"


class CarGroup(CarItemBase):
    class Meta:
        verbose_name = "Штатная группа"
        verbose_name_plural = "Штатные группы"


class GasolineBrand(CarItemBase):
    class Meta:
        verbose_name = "Марка Бензина"
        verbose_name_plural = "Марки бензина"


class CarClass(CarItemBase):
    class Meta:
        verbose_name = "Класс Автотранспорта"
        verbose_name_plural = "Классы Автотранспорта"


class Color(CarItemBase):
    class Meta:
        verbose_name = "Цвет Автотранспорта"
        verbose_name_plural = "Цвета Автотранспорта"


class MaintenanceService(CarItemBase):
    class Meta:
        verbose_name = "Служба эксплуатации автомобиля"
        verbose_name_plural = "Службы эксплутации автомобиля"


class Source(CarItemBase):
    class Meta:
        verbose_name = "Организ., выдавшая наряд"
        verbose_name_plural = "Организ., выдавшая наряд"


class Warehouse(CarItemBase):
    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"
