import csv
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from django.db import models, transaction
from django.core.management.base import BaseCommand

from configs.settings import DATA_PATH
from vehicles.models import (
    VehicleType, VehicleBody, VehicleClass, VehicleGroup, Color, Manufacturer, Brand, Source,
    MaintenanceService, Warehouse, Waybill, FuelType, Subdivision, Engine,
    Passport, Distribution, Vehicle
)


class Command(BaseCommand):
    mapping_fields = {
        'inventory_number': {
            'row_index': 0,
            'type': int
        },
        'year': {
            'row_index': 9,
            'type': int
        },
        'chass_number': {
            'row_index': 6,
            'type': str
        },
        'gov_number': {
            'row_index': 12,
            'type': str
        },
        'register_number': {
            'row_index': 13,
            'type': str
        },
        'sign_date': {
            'row_index': 15,
            'type': date
        },
        'exploitation_date': {
            'row_index': 16,
            'type': date
        },
        'base_rate': {
            'row_index': 47,
            'type': Decimal,
        },
        'identifier_fuel_rate': {
            'row_index': 48,
            'type': Decimal
        },
        'source_number': {
            'row_index': 26,
            'type': str
        },
        'source_date': {
            'row_index': 27,
            'type': date
        },
        'transfer_date': {
            'row_index': 33,
            'type': date
        },
        'climate_control': {
            'row_index': 45,
            'type': bool
        },
        'mileage_rate': {
            'row_index': 35,
            'type': Decimal
        },
        'fuel_rate': {
            'row_index': 36,
            'type': Decimal
        },
        'id_number': {
            'row_index': 40,
            'type': str
        },
        'category': {
            'row_index': 49,
            'type': str
        },
        'trust_date': {
            'row_index': 50,
            'type': date
        },
        'to_date': {
            'row_index': 51,
            'type': date
        },
        'cost': {
            'row_index': 22,
            'type': Decimal
        }
    }

    mapping_relational_fields = {
        'engine': {
            'fields': {
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
            'model': Engine
        },
        'passport': {
            'fields': {
                'number': {
                    'row_index': 10,
                    'type': str,
                },
                'date': {
                    'row_index': 11,
                    'type': date,
                }
            },
            'model': Passport
        },
        'distribution': {
            'fields': {
                'number': {
                    'row_index': 31,
                    'type': str,
                },
                'date': {
                    'row_index': 32,
                    'type': date,
                }
            },
            'model': Distribution
        },
        'waybill': {
            'fields': {
                'number': {
                    'row_index': 29,
                    'type': str,
                },
                'date': {
                    'row_index': 30,
                    'type': date,
                }
            },
            'model': Waybill
        },
        'type': {
            'fields': {
                'code': {
                    'row_index': 1,
                    'type': str,
                }
            },
            'model': VehicleType
        },
        'manufacturer': {
            'fields': {
                'code': {
                    'row_index': 2,
                    'type': str,
                }
            },
            'model': Manufacturer
        },
        'brand': {
            'fields': {
                'code': {
                    'row_index': 3,
                    'type': str,
                }
            },
            'model': Brand
        },
        'body': {
            'fields': {
                'code': {
                    'row_index': 4,
                    'type': str,
                }
            },
            'model': VehicleBody
        },
        'group': {
            'fields': {
                'code': {
                    'row_index': 5,
                    'type': str,
                }
            },
            'model': VehicleGroup
        },
        'vehicle_class': {
            'fields': {
                'code': {
                    'row_index': 17,
                    'type': str,
                }
            },
            'model': VehicleClass
        },
        'color': {
            'fields': {
                'code': {
                    'row_index': 18,
                    'type': str,
                }
            },
            'model': Color
        },
        'source': {
            'fields': {
                'code': {
                    'row_index': 25,
                    'type': str,
                }
            },
            'model': Source
        },
        'warehouse': {
            'fields': {
                'code': {
                    'row_index': 28,
                    'type': str,
                }
            },
            'model': Warehouse
        },
        'fuel_type': {
            'fields': {
                'code': {
                    'row_index': 42,
                    'type': str,
                }
            },
            'model': FuelType
        },
        'service': {
            'fields': {
                'code': {
                    'row_index': 19,
                    'type': str,
                }
            },
            'model': MaintenanceService
        },
        'subdivision': {
            'fields': {
                'code': {
                    'row_index': 20,
                    'type': str,
                }
            },
            'model': Subdivision
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
            return datetime.strptime(date, '%d.%m.%Y').date()
        return None

    def _parse_decimal(self, numeric: str) -> Decimal | None:
        numeric.replace(',', '.')
        try:
            return Decimal(numeric)
        except InvalidOperation:
            return None

    def _parse_int(self, number: str) -> int | None:
        if number.isdigit():
            return int(number)
        return None

    def _parse_str(self, value: str) -> str | None:
        if value == '':
            return None
        return value

    def _parse_bool(self, value: str) -> bool | None:
        if value.isdigit():
            return bool(int(value))
        return None

    def _parse_column(
        self, type_: str | int | Decimal | date | bool, value: str
    ) -> str | int | Decimal | date | None:
        if type_ == int:
            return self._parse_int(value)

        elif type_ == date:
            return self._parse_date(value)

        elif type_ == Decimal:
            return self._parse_decimal(value)

        elif type_ == str:
            return self._parse_str(value)

        elif type_ == bool:
            return self._parse_bool(value)

        return value

    @transaction.atomic
    def handle(self, *args, **options):
        with open(DATA_PATH / 'AUTO.csv', newline='') as auto:
            reader = csv.reader(auto, delimiter=',')
            next(reader)
            for row in reader:
                vehicle_values = {}
                for field, data in self.mapping_fields.items():
                    value: str = row[data['row_index']]
                    type_: str | int | Decimal | date | bool = data['type']
                    vehicle_values[field] = self._parse_column(type_, value)

                for field, data in self.mapping_relational_fields.items():
                    model = data['model']
                    obj_values = {}
                    for obj_field, obj_data in data['fields'].items():
                        value: str = row[obj_data['row_index']]
                        type_: str | int | Decimal | date | bool = obj_data['type']
                        obj_values[obj_field] = self._parse_column(type_, value)

                    vehicle_values[field] = self._get_or_create(model, **obj_values)

                Vehicle.objects.create(**vehicle_values)
