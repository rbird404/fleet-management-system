from django.db import models
from django.core.validators import MaxValueValidator


class CarType(models.Model):
    CSV_CODE = "A"
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Тип транспортного средства"
        verbose_name_plural = "Типы Транспортных средств"


class Manufacturer(models.Model):
    CSV_CODE = "C"
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Завод Изготовитель"
        verbose_name_plural = "Заводы Изготовителя"


class Brand(models.Model):
    CSV_CODE = "B"
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Марка транспортного средства"
        verbose_name_plural = "Марки Транспортных средств"


class CarBody(models.Model):
    CSV_CODE = "D"
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Тип Кузова"
        verbose_name_plural = "Тип Кузовов"


class CarGroup(models.Model):
    CSV_CODE = "E"
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Штатная группа"
        verbose_name_plural = "Штатные группы"


class GasolineBrand(models.Model):
    CSV_CODE = "c"
    name = models.CharField(max_length=6)
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Марка Бензина"
        verbose_name_plural = "Марки бензина"


class CarClass(models.Model):
    CSV_CODE = "F"
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Класс Автотранспорта"
        verbose_name_plural = "Классы Автотранспорта"


class Color(models.Model):
    CSV_CODE = "G"
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Цвет Автотранспорта"
        verbose_name_plural = "Цвета Автотранспорта"


class MaintenanceService(models.Model):
    CSV_CODE = "H"
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Служба эксплуатации автомобиля"
        verbose_name_plural = "Службы эксплутации автомобиля"


class Structure(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(
        max_length=35,
        null=True, blank=True,
        verbose_name="Название Подразделения"
    )
    phone = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name="Телефон"
    )
    chief = models.CharField(
        max_length=35,
        null=True, blank=True,
        verbose_name="Начальник Подразделения"
    )
    percent_city = models.IntegerField(
        validators=[MaxValueValidator(99)],
        null=True, blank=True,
        verbose_name="Процент города"
    )
    parent = models.ForeignKey(
        "self",
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Подразделение-владелец транспорта"
        verbose_name_plural = "Подразделения-владельцы транспорта"


class Source(models.Model):
    CSV_CODE = "I"
    name = models.CharField(
        max_length=128,
        null=True, blank=True
    )
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Организ., выдавшая наряд"
        verbose_name_plural = "Организ., выдавшая наряд"


class Warehouse(models.Model):
    CSV_CODE = "J"
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"


class Engine(models.Model):
    number = models.CharField(
        verbose_name="Номер Двигателя",
        max_length=16,
        null=True,
        blank=True
    )
    model = models.CharField(
        verbose_name="Модель двигателя т/c",
        max_length=15,
        null=True,
        blank=True
    )
    power = models.IntegerField(
        verbose_name="Мощность двигателя т/c",
        validators=[MaxValueValidator(999)],
        null=True,
        blank=True
    )
    capacity = models.DecimalField(
        verbose_name="Объем двигателя т/с",
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.number} {self.model}"

    class Meta:
        verbose_name = "Двигатель Т/C"
        verbose_name_plural = "Двигатели Т/C"


class Waybill(models.Model):
    number = models.CharField(
        verbose_name="Номер накладной",
        max_length=16,
        null=True,
        blank=True
    )
    date = models.DateField(
        verbose_name="Дата накладной",
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.number} {self.date}"

    class Meta:
        verbose_name = "Накладная"
        verbose_name_plural = "Накладные"


class Distribution(models.Model):
    number = models.CharField(
        verbose_name="Номер распределения",
        max_length=15,
        null=True,
        blank=True
    )
    date = models.DateField(
        verbose_name="Дата распределения",
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.number} {self.date}"

    class Meta:
        verbose_name = "Распределение"
        verbose_name_plural = "Распределения"


class Passport(models.Model):
    number = models.CharField(
        verbose_name="Номер тех. паспорта",
        max_length=10,
        null=True,
        blank=True
    )
    date = models.DateField(
        verbose_name="Дата выдачи тех. паспорта",
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.number} {self.date}"

    class Meta:
        verbose_name = "Тех. паспорт"
        verbose_name_plural = "Тех. паспорта"


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
        blank=True
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        verbose_name="Завод-Изготовитель",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    brand = models.ForeignKey(
        Brand,
        verbose_name="Марка",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    body = models.ForeignKey(
        CarBody,
        verbose_name="Тип Кузова",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        CarGroup,
        verbose_name="Штатная группа",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    chass_number = models.CharField(
        verbose_name="Номер Шасси",
        max_length=8,
        null=True,
        blank=True
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
        blank=True,
    )
    passport = models.OneToOneField(
        Passport,
        verbose_name="Тех. паспорт",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    sign = models.CharField(
        verbose_name="Номер государственной регистрации",
        max_length=16,
        null=True,
        blank=True
    )
    sign1 = models.CharField(
        verbose_name="Реестровый номер",
        max_length=16,
        null=True,
        blank=True
    )
    sign2 = models.CharField(
        verbose_name="Дубль 2",
        max_length=16,
        null=True,
        blank=True
    )
    sign_date = models.DateField(
        verbose_name="Дата выдачи номерного знака",
        null=True,
        blank=True
    )
    exploitation_date = models.DateField(
        verbose_name="Дата ввода в эксплутацию",
        null=True,
        blank=True,
    )
    car_class = models.ForeignKey(
        CarClass,
        verbose_name="Класс автомобиля",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    color = models.ForeignKey(
        Color,
        verbose_name="Цвет автомобиля",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    service = models.ForeignKey(
        MaintenanceService,
        verbose_name="Служба эксплутации",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        Structure,
        verbose_name="Подразделение-владелец транспорта",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    cost = models.DecimalField(
        verbose_name="Балансовая стоимость",
        max_digits=18,
        decimal_places=2,
        null=True,
        blank=True,
    )
    source = models.ForeignKey(
        Source,
        verbose_name="Источник получения",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    source_number = models.CharField(
        verbose_name="Номер Фондового извещения",
        max_length=16,
        null=True,
        blank=True
    )
    source_date = models.DateField(
        verbose_name="Дата документа",
        null=True,
        blank=True
    )
    warehouse = models.ForeignKey(
        Warehouse,
        verbose_name="Склад",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    waybill = models.OneToOneField(
        Waybill,
        verbose_name="Накладная",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    distribution = models.OneToOneField(
        Distribution,
        verbose_name="Распределение",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    transfer_date = models.DateField(
        verbose_name="Дата передачи в подразделение",
        null=True,
        blank=True
    )
    del_date = models.DateField(
        verbose_name="Дата списания",
        null=True,
        blank=True
    )
    mileage_rate = models.DecimalField(
        verbose_name="Месячная норма пробега",
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )
    fuel_rate = models.DecimalField(
        verbose_name="Норма расхода топлива на 100 км",
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    id_number = models.CharField(
        verbose_name="Идентификационный номер",
        max_length=20,
        null=True,
        blank=True
    )
    gasoline_brand = models.ForeignKey(
        GasolineBrand,
        verbose_name="Марка бензина",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
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
        blank=True,
    )
    base_rate = models.DecimalField(
        verbose_name="Базовая норма расхода топлива",
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )
    identifier_fuel_rate = models.IntegerField(
        verbose_name="Инд. процент баз. нормы расхода топлива",
        validators=[MaxValueValidator(999)],
        null=True,
        blank=True,
    )
    category = models.CharField(
        choices=CATEGORIES,
        verbose_name="Категория автомобиля",
        max_length=1,
        null=True,
        blank=True
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
        return f"Auto inv#{self.inventory_number}"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
