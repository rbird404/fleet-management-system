import csv
from typing import Any, Optional
from django.core.management import BaseCommand

from configs.settings import DATA_PATH
from cars.models import Subdivision


class Command(BaseCommand):
    def _create_subdivision(self, row, parent=None):
        return Subdivision.objects.create(
            code=row[0] + row[1] + row[2],
            name=row[3],
            chief=row[5],
            phone=row[-2],
            parent=parent
        )

    def _create_subdivisions(
        self, level: int, parent: Subdivision | None = None
    ) -> list[Subdivision]:
        subdivisions = []

        with open(DATA_PATH / 'STRUC.csv', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                if level == 1:
                    if row[1] == "":
                        subdivisions.append(
                            self._create_subdivision(row, None)
                        )

                elif level == 2 and parent is not None:
                    row_code = row[0] + row[1] + row[2]
                    if (row[1] != "" and row[2] == "" and
                            row_code.startswith(parent.code)):
                        subdivisions.append(
                            self._create_subdivision(row, parent)
                        )

                elif level == 3 and parent is not None:
                    row_code = row[0] + row[1] + row[2]
                    if (row[1] != "" and row[2] != "" and
                            row_code.startswith(parent.code)):
                        subdivisions.append(
                            self._create_subdivision(row, parent)
                        )

        return subdivisions

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        subdivisions_first_lvl = self._create_subdivisions(level=1, parent=None)
        subdivisions_second_lvl = []
        for structure in subdivisions_first_lvl:
            subdivisions_second_lvl.extend(
                self._create_subdivisions(level=2, parent=structure)
            )

        for structure in subdivisions_second_lvl:
            self._create_subdivisions(
                level=3, parent=structure
            )

        return None
