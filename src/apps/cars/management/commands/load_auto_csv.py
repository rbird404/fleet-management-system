import csv
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from configs.settings import DATA_PATH
from apps.cars.models import *
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    mapping = {
        1: {
            "field": 'type',
            "model": CarType
        },
        2: {
            "field": 'manufacturer',
            "model": Manufacturer
        },
        3: {
            "field": 'brand',
            "model": Brand
        },
        4: {
            "field": 'body',
            "model": CarBody
        },
        5: {
            "field": 'group',
            "model": CarGroup
        },
        17: {
            "field": 'car_class',
            "model": CarClass
        },
        18: {
            "field": 'color',
            "model": Color
        },
        25: {
            "field": 'source',
            "model": Source
        },
        28: {
            "field": 'warehouse',
            "model": Warehouse
        },
        42: {
            "field": 'gasoline_brand',
            "model": GasolineBrand
        },
        19: {
            "field": 'service',
            "model": MaintenanceService
        },
        20: {
            "field": 'subdivision',
            "model": Subdivision
        }
    }

    def _get_or_none(self, model: models.Model, **kwargs) -> models.Model | None:
        try:
            return model.objects.get(**kwargs)
        except model.DoesNotExist:
            return None

    def _parse_date(self, date: str) -> date | None:
        if date:
            return datetime.strptime(date, "%d.%m.%Y").date()
        return None

    def _parse_decimal(self, numeric: str) -> Decimal | None:
        numeric.replace(",", ".")
        try:
            return Decimal(numeric)
        except InvalidOperation:
            return None

    def _parse_int(self, number: str) -> int | None:
        if number.isdigit():
            return int(number)

        return None

    def _create_mapping_models(self, row: str) -> dict:
        result = {}
        for row_index, data in self.mapping.items():
            result[data['field']] = self._get_or_none(
                data['model'], code=row[row_index]
            )

        return result

    def _create_engine(self, row):
        engine_number = row[7]
        engine_mark = row[43]
        engine_power = self._parse_int(row[44])
        engine_capacity = self._parse_decimal(row[46])
        engine = Engine.objects.create(
            number=engine_number,
            model=engine_mark,
            power=engine_power,
            capacity=engine_capacity
        )
        return engine

    def handle(self, *args, **options):
        with open(DATA_PATH / 'AUTO.csv', newline='') as auto:
            reader = csv.reader(auto, delimiter=',')
            next(reader)
            for row in reader:
                fields = self._create_mapping_models(row)
                inventory_number = self._parse_int(row[0])
                year = self._parse_int(row[9])
                chass_number = row[6]

                passport_number = row[10]
                passport_date = self._parse_date(row[11])

                sign = row[12]
                sign1 = row[13]

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

                mileage_rate = self._parse_decimal(row[35])
                fuel_rate = self._parse_decimal(row[36])
                id_number = row[40]

                category = row[49]
                trust_date = self._parse_date(row[50])
                to_date = self._parse_date(row[51])
                cost = self._parse_decimal(row[22])

                engine = self._create_engine(row)

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
                    **fields,
                    inventory_number=inventory_number,
                    year=year,
                    chass_number=chass_number,
                    passport=passport,
                    gov_number=sign,
                    register_number=sign1,
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
                    source_number=source_number,
                    source_date=source_date,
                    cost=cost
                )
