import csv
from typing import Any, Optional
from django.core.management.base import BaseCommand
from configs.settings import DATA_PATH
from apps.cars.models import Structure


class Command(BaseCommand):

    def _create_structure(self, row, parent=None):
        return Structure.objects.create(
            code=row[0] + row[1] + row[2],
            name=row[3],
            chief=row[5],
            phone=row[-2],
            parent=parent
        )

    def _create_structures(
        self, level: int, parent: Structure | None = None
    ) -> list[Structure]:
        structures = []

        with open(DATA_PATH / 'STRUC.csv', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                if level == 1:
                    if row[1] == "":
                        structures.append(
                            self._create_structure(row, None)
                        )

                elif level == 2 and parent is not None:
                    row_code = row[0] + row[1] + row[2]
                    if (row[1] != "" and row[2] == "" and
                            row_code.startswith(parent.code)):
                        structures.append(
                            self._create_structure(row, parent)
                        )

                elif level == 3 and parent is not None:
                    row_code = row[0] + row[1] + row[2]
                    if (row[1] != "" and row[2] != "" and
                            row_code.startswith(parent.code)):
                        structures.append(
                            self._create_structure(row, parent)
                        )

        return structures

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        structures_first_lvl = self._create_structures(level=1, parent=None)
        structures_second_lvl = []
        for structure in structures_first_lvl:
            structures_second_lvl.extend(
                self._create_structures(level=2, parent=structure)  
            )

        for structure in structures_second_lvl:
            self._create_structures(
                level=3, parent=structure
            )

        return "SUCCESS"
