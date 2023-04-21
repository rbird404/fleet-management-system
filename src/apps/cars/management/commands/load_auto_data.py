from django.core.management.base import BaseCommand
from datetime import datetime
from decimal import Decimal, InvalidOperation
import csv
from configs.settings import DATA_PATH
from apps.cars.models import *


class Command(BaseCommand):
    def _get_or_none(self, model, **kwargs):
        result = None
        try:
            result = model.objects.get(**kwargs)
        except model.DoesNotExist:
            result = None

        return result

    def _parse_date(self, date: str) -> datetime | None:
        try:
            return datetime.strptime(date, "%d.%m.%Y").date()
        except ValueError:
            return None

    def _parse_decimal(self, numeric: str) -> Decimal | None:
        numeric.replace(",", ".")
        try:
            return Decimal(numeric)
        except InvalidOperation:
            return None

    def _parse_int(self, number: str) -> int | None:
        try:
            return int(number)
        except ValueError:
            return None

    def handle(self, *args, **options):
        with open(DATA_PATH / 'AUTO.csv', newline='') as auto:
            reader = csv.reader(auto, delimiter=',')
            next(reader)
            for row in reader:
                type_ = self._get_or_none(CarType, code=row[1])
                manufacturer = self._get_or_none(Manufacturer, code=row[2])
                brand = self._get_or_none(Brand, code=row[3])
                body = self._get_or_none(CarBody, code=row[4])
                group = self._get_or_none(CarGroup, code=row[5])
                car_class = self._get_or_none(CarClass, code=row[17])
                color = self._get_or_none(Color, code=row[18])
                source = self._get_or_none(Source, code=row[25])
                warehouse = self._get_or_none(Warehouse, code=row[28])
                gasoline_brand = self._get_or_none(GasolineBrand, code=row[42])
                service = self._get_or_none(MaintenanceService, code=row[19])
                owner = self._get_or_none(Structure, code=row[20])

                inventory_number = self._parse_int(row[0])
                year = self._parse_int(row[9])
                chass_number = row[6]
                engine_number = row[7]
                passport_number = row[10]
                passport_date = self._parse_date(row[11])

                sign = row[12]
                sign1 = row[13]
                sign2 = row[14]

                sign_date = self._parse_date(row[15])
                body_number = row[8]
                exploitation_date = self._parse_date(row[16])

                base_rate = self._parse_decimal(row[47])
                identifier_fuel_rate = self._parse_decimal(row[48])

                source_number = row[26]
                source_date = self._parse_date(row[27])
                waybill_number = row[29]
                waybill_date = self._parse_date(row[30])
                distribution_number = row[31]
                distribution_date = self._parse_date(row[32])
                transfer_date = self._parse_date(row[33])

                climate_control = self._parse_int(row[45])
                if climate_control:
                    climate_control = bool(climate_control)

                engine_mark = row[43]
                mileage_rate = self._parse_decimal(row[35])
                fuel_rate = self._parse_decimal(row[36])
                id_number = row[40]
                engine_power = self._parse_int(row[44])
                engine_capacity = self._parse_decimal(row[46])
                category = row[49]
                trust_date = self._parse_date(row[50])
                to_date = self._parse_date(row[51])
                cost = self._parse_decimal(row[22])

                engine = Engine.objects.create(
                    number=engine_number,
                    model=engine_mark,
                    power=engine_power,
                    capacity=engine_capacity
                )
                passport = Passport.objects.create(
                    number=passport_number,
                    date=passport_date
                )
                distribution = Distribution.objects.create(
                    number=distribution_number,
                    date=distribution_date
                )
                waybill = Waybill.objects.create(
                    number=waybill_number,
                    date=waybill_date
                )

                Car.objects.create(
                    type=type_,
                    manufacturer=manufacturer,
                    body=body,
                    brand=brand,
                    cost=cost,
                    group=group,
                    car_class=car_class,
                    owner=owner,
                    service=service,
                    warehouse=warehouse,
                    gasoline_brand=gasoline_brand,
                    inventory_number=inventory_number,
                    year=year,
                    color=color,
                    chass_number=chass_number,
                    passport=passport,
                    sign=sign,
                    sign1=sign1,
                    sign2=sign2,
                    sign_date=sign_date,
                    body_number=body_number,
                    exploitation_date=exploitation_date,
                    waybill=waybill,
                    distribution=distribution,
                    transfer_date=transfer_date,
                    mileage_rate=mileage_rate,
                    fuel_rate=fuel_rate,
                    id_number=id_number,
                    engine=engine,
                    climate_control=climate_control,
                    base_rate=base_rate,
                    identifier_fuel_rate=identifier_fuel_rate,
                    category=category,
                    trust_date=trust_date,
                    to_date=to_date,
                    source=source,
                    source_number=source_number,
                    source_date=source_date
                )
