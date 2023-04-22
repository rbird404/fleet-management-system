import csv
from configs.settings import DATA_PATH
from django.core.management.base import BaseCommand
from cars.models import (
    CarType, Manufacturer, Brand, CarBody,
    CarGroup, GasolineBrand, CarClass, Color,
    MaintenanceService, Source, Warehouse,
)


class Command(BaseCommand):

    mapping = {
        "A": CarType,
        "C": Manufacturer,
        "B": Brand,
        "D": CarBody,
        "E": CarGroup,
        "c": GasolineBrand,
        "F": CarClass,
        "G": Color,
        "H": MaintenanceService,
        "I": Source,
        "j": Warehouse,
    }

    def handle(self, *args, **options):
        with open(DATA_PATH / 'MENU.csv', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                for code, model in self.mapping.items():
                    # row[1] unique obj id
                    if code == row[0] and row[1] != "":
                        model.objects.create(
                            name=row[2],
                            code=row[0] + row[1],
                        )
