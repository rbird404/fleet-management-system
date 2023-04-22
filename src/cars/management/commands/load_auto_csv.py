import csv
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from django.db import models
from django.core.management.base import BaseCommand

from configs.settings import DATA_PATH
from cars.models import (
    CarType, CarBody, CarClass, CarGroup, Color, Manufacturer, Brand, Source,
    MaintenanceService, Warehouse, Waybill, GasolineBrand, Subdivision, Engine,
    Passport, Distribution, Car
)


class Command(BaseCommand):
    mapping_csv_colum = {
        0: {
            'field': 'inventory_number',
            'type': int
        },
        9: {
            'field': 'year',
            'type': int
        },
        6: {
            'field': 'chass_number',
            'type': str
        },
        12: {
            'field': 'gov_number',
            'type': str
        },
        13: {
            'field': 'register_number',
            'type': str
        },
        15: {
            'field': 'sign_date',
            'type': date
        },
        16: {
            'field': 'exploitation_date',
            'type': date
        },
        47: {
            'field': 'base_rate',
            'type': Decimal,
        },
        48: {
            'field': 'identifier_fuel_rate',
            'type': Decimal
        },
        26: {
            'field': 'source_number',
            'type': str
        },
        27: {
            'field': 'source_date',
            'type': date
        },
        33: {
            'field': 'transfer_date',
            'type': date
        },
        45: {
            'field': 'climate_control',
            'type': bool
        },
        35: {
            'field': 'mileage_rate',
            'type': Decimal
        },
        36: {
            'field': 'fuel_rate',
            'type': Decimal
        },
        40: {
            'field': 'id_number',
            'type': str
        },
        49: {
            'field': 'category',
            'type': str
        },
        50: {
            'field': 'trust_date',
            'type': date
        },
        51: {
            'field': 'to_date',
            'type': date
        },
        22: {
            'field': 'cost',
            'type': Decimal
        }
    }

    mapping_relation = {
        'engine': {
            "fields": {
                'number': {
                    'row_index': 7,
                    'type': int,
                },
                'model': {
                    'row_index': 43,
                    'type': str,
                },
                'power': {
                    'row_index': 44,
                    'type': int
                },
                'capacity': {
                    'row_index': 46,
                    'type': Decimal
                }
            },
            "model": Engine
        },
        'passport': {
            "fields": {
                'number': {
                    'row_index': 10,
                    'type': str,
                },
                'date': {
                    'row_index': 11,
                    'type': date,
                }
            },
            "model": Passport
        },
        'distribution': {
            "fields": {
                'number': {
                    'row_index': 31,
                    'type': str,
                },
                'date': {
                    'row_index': 32,
                    'type': date,
                }
            },
            "model": Distribution
        },
        'waybill': {
            "fields": {
                'number': {
                    'row_index': 29,
                    'type': str,
                },
                'date': {
                    'row_index': 30,
                    'type': date,
                }
            },
            "model": Waybill
        },
        'type': {
            "fields": {
                'code': {
                    'row_index': 1,
                    'type': str,
                }
            },
            "model": CarType
        },
        'manufacturer': {
            "fields": {
                'code': {
                    'row_index': 2,
                    'type': str,
                }
            },
            "model": Manufacturer
        },
        'brand': {
            "fields": {
                'code': {
                    'row_index': 3,
                    'type': str,
                }
            },
            "model": Brand
        },
        'body': {
            "fields": {
                'code': {
                    'row_index': 4,
                    'type': str,
                }
            },
            "model": CarBody
        },
        'group': {
            "fields": {
                'code': {
                    'row_index': 5,
                    'type': str,
                }
            },
            "model": CarGroup
        },
        'car_class': {
            "fields": {
                'code': {
                    'row_index': 17,
                    'type': str,
                }
            },
            "model": CarClass
        },
        'color': {
            "fields": {
                'code': {
                    'row_index': 18,
                    'type': str,
                }
            },
            "model": Color
        },
        'source': {
            "fields": {
                'code': {
                    'row_index': 25,
                    'type': str,
                }
            },
            "model": Source
        },
        'warehouse': {
            "fields": {
                'code': {
                    'row_index': 28,
                    'type': str,
                }
            },
            "model": Warehouse
        },
        'gasoline_brand': {
            "fields": {
                'code': {
                    'row_index': 42,
                    'type': str,
                }
            },
            "model": GasolineBrand
        },
        'service': {
            "fields": {
                'code': {
                    'row_index': 19,
                    'type': str,
                }
            },
            "model": MaintenanceService
        },
        'subdivision': {
            "fields": {
                'code': {
                    'row_index': 20,
                    'type': str,
                }
            },
            "model": Subdivision
        }
    }
    _one_to_one_models = (Engine, Distribution, Waybill, Passport)

    def _get_or_create(self, model_class: models.Model, **kwargs) -> models.Model | None:
        if model_class in self._one_to_one_models:
            return model_class.objects.create(**kwargs)
        try:
            return model_class.objects.get(**kwargs)
        except model_class.DoesNotExist:
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

    def _parse_column(
        self, type_: str | int | Decimal | date, value: str
    ) -> str | int | Decimal | date | None:
        if type_ == int:
            return self._parse_int(value)

        elif type_ == date:
            return self._parse_date(value)

        elif type_ == Decimal:
            return self._parse_decimal(value)

        return value

    def handle(self, *args, **options):
        with open(DATA_PATH / 'AUTO.csv', newline='') as auto:
            reader = csv.reader(auto, delimiter=',')
            next(reader)
            for row in reader:
                car_values = {}
                for index, data in self.mapping_csv_colum.items():
                    value: str = row[index]
                    type_: str | int | Decimal | date = data['type']
                    field: str = data['field']
                    car_values[field] = self._parse_column(type_, value)

                for field, data in self.mapping_relation.items():
                    model = data['model']
                    obj_values = {}
                    for obj_field, obj_data in data['fields'].items():
                        value: str = row[obj_data['row_index']]
                        type_: str | int | Decimal | date = obj_data['type']
                        obj_values[obj_field] = self._parse_column(type_, value)

                    car_values[field] = self._get_or_create(model, **obj_values)

                Car.objects.create(**car_values)
