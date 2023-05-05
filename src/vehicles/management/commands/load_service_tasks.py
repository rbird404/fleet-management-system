import csv
from django.core.management.base import BaseCommand
from django.db import transaction

from configs.settings import DATA_PATH
from maintenance.models import Task


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        with open(DATA_PATH / 'MENU_CH.csv', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for index, row in enumerate(reader, start=1):
                Task.objects.create(
                    order=index, name=row[2]
                )
