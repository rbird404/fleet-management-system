import csv
from datetime import datetime, date

from django.core.management.base import BaseCommand

from configs.settings import DATA_PATH
from history.models import History
from cars.models import (
    Brand, CarBody, CarGroup, Color,
    MaintenanceService, Engine, Passport, Subdivision, Car
)


class Command(BaseCommand):
    mapping_one_to_one = {
        6: {
            'field': 'body',
            'change_field': 'number',
            'type': 'str',
            'model': CarBody,
        },
        5: {
            'field': 'engine',
            'change_field': 'number',
            'type': 'str',
            'model': Engine,
        },
        10: {
            'field': 'passport',
            'change_field': 'number',
            'type': 'str',
            'model': Passport
        }
    }
    mapping_fields = {
        8: 'chass_number',
        17: 'date_del',
        11: 'gov_number',
        12: 'register_number'
    }

    mapping_one_to_many = {
        9: {
            'field': 'color',
            'model': Color
        },
        13: {
            'field': 'subdivision',
            'model': Subdivision
        },
        21: {
            'field': 'brand',
            'model': Brand
        },
        22: {
            'field': 'body',
            'model': CarBody
        },
        23: {
            'field': 'group',
            'model': CarGroup
        },
        28: {
            'field': 'subdivision',
            'model': Subdivision
        },
        30: {
            'field': 'service',
            'model': MaintenanceService
        },
    }

    def _parse_date(self, date: str) -> date | None:
        if date:
            return datetime.strptime(date, '%d.%m.%Y').date()
        return None

    def handle(self, *args, **options):
        with open(DATA_PATH / 'CHANGE.csv', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for index, row in enumerate(reader, start=1):
                inv_number = row[0]  # inventory_number
                try:
                    car = Car.objects.get(inventory_number=inv_number)
                except Car.DoesNotExist:
                    continue
                change_index = int(row[1])
                if change_index in self.mapping_fields:
                    data = {
                        'content_object': car,
                        'field': self.mapping_fields[change_index],
                        'value': row[2],
                        'value_type': 'str',
                    }

                elif change_index in self.mapping_one_to_one:
                    change_data = self.mapping_one_to_one.get(change_index)
                    obj = getattr(car, change_data['field'])
                    data = {
                        'content_object': obj,
                        'value': row[2],
                        'field': change_data['change_field'],
                        'value_type': change_data['type'],
                    }

                elif change_index in self.mapping_one_to_many:
                    change_data = self.mapping_one_to_many.get(change_index)
                    model = change_data['model']
                    field = change_data['field']
                    try:
                        obj = model.objects.get(code=row[2])
                    except model.DoesNotExist:
                        continue
                    data = {
                        'content_object': car,
                        'value': obj.id,
                        'field': field,
                        'value_type': 'int'
                    }
                else:
                    continue

                data['created_at'] = self._parse_date(row[3])
                History.objects.create(**data)
