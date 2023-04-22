import csv
from django.core.management.base import BaseCommand
from configs.settings import DATA_PATH
from apps.cars.models import (
    CarType,
    Manufacturer,
    Brand,
    CarBody,
    CarGroup,
    GasolineBrand,
    CarClass,
    Color,
    MaintenanceService,
    Source,
    Warehouse,
)


class Command(BaseCommand):

    models = [
        CarType,
        Manufacturer,
        Brand,
        CarBody,
        CarGroup,
        GasolineBrand,
        CarClass,
        Color,
        MaintenanceService,
        Source,
        Warehouse,
    ]

    def handle(self, *args, **options):
        with open(DATA_PATH / 'MENU.csv', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                for model in self.models:
                    if model.CSV_CODE == row[0] and row[1] != "":  # TODO: Опять же маппинг, так как тут Magick Number
                        model.objects.create(
                            name=row[2],
                            code=row[0] + row[1],
                        )
