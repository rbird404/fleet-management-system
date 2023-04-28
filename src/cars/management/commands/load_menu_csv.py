import csv
from django.db import transaction
from django.core.management.base import BaseCommand

from configs.settings import DATA_PATH
from cars.models import (
    CarType, Manufacturer, Brand, CarBody,
    CarGroup, GasolineBrand, CarClass, Color,
    MaintenanceService, Source, Warehouse
)


class Command(BaseCommand):

    mapping_models = {
        'A': CarType,
        'C': Manufacturer,
        'B': Brand,
        'D': CarBody,
        'E': CarGroup,
        'c': GasolineBrand,
        'F': CarClass,
        'G': Color,
        'H': MaintenanceService,
        'I': Source,
        'J': Warehouse,
        'N': Brand,
        'X': Brand,
        'O': Brand,
        'P': Brand,
        'Q': Brand,
        'R': Brand,
        'S': Brand,
        'T': Brand,
    }

    mapping_fields = {
        'name': {
            'row_index': 2,
            'type': str
        },
        'code': {
            'row_index': slice(0, 2),
            'type': str
        }
    }

    @transaction.atomic
    def handle(self, *args, **options):
        with open(DATA_PATH / 'MENU.csv', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                for model_code, model in self.mapping_models.items():
                    # row[0] table id
                    # row[1] unique obj id
                    if model_code == row[0] and row[1] != '':
                        values = {}
                        for field, data in self.mapping_fields.items():
                            value = row[data['row_index']]

                            if isinstance(data['row_index'], slice):
                                value = ''.join(value)
                            else:
                                if value == '':
                                    value = None

                            values[field] = value

                        model.objects.create(**values)
