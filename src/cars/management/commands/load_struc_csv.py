import csv
from typing import Any, Optional
from django.core.management import BaseCommand

from configs.settings import DATA_PATH
from cars.models import Subdivision


class Command(BaseCommand):
    mapping_fields = {
        'name': {
            'row_index': 3,
            'type': str
        },
        'chief': {
            'row_index': 5,
            'type': str
        },
        'phone': {
            'row_index': 7,
            'type': str
        },
        'code': {
            'row_index': slice(0, 3),
            'type': str
        }
    }

    def _create_subdivision(self, row, parent=None):
        values = {}
        for field, data in self.mapping_fields.items():
            value = row[data['row_index']]

            if isinstance(data['row_index'], slice):
                value = ''.join(value)
            values[field] = value

        values['parent'] = parent
        return Subdivision.objects.create(**values)

    def _create_subdivisions(
        self, level: int, parent: Subdivision | None = None
    ) -> list[Subdivision]:
        subdivisions = []

        with open(DATA_PATH / 'STRUC.csv', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                if level == 1:
                    if row[1] == '':
                        subdivisions.append(
                            self._create_subdivision(row, None)
                        )

                elif level == 2 and parent is not None:
                    row_code = row[0] + row[1] + row[2]
                    if (row[1] != '' and row[2] == '' and
                            row_code.startswith(parent.code)):
                        subdivisions.append(
                            self._create_subdivision(row, parent)
                        )

                elif level == 3 and parent is not None:
                    row_code = row[0] + row[1] + row[2]
                    if (row[1] != '' and row[2] != '' and
                            row_code.startswith(parent.code)):
                        subdivisions.append(
                            self._create_subdivision(row, parent)
                        )

        return subdivisions

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        subdivisions_first_lvl = self._create_subdivisions(level=1, parent=None)
        subdivisions_second_lvl = []
        for subdivision in subdivisions_first_lvl:
            subdivisions_second_lvl.extend(
                self._create_subdivisions(level=2, parent=subdivision)
            )

        for subdivision in subdivisions_second_lvl:
            self._create_subdivisions(
                level=3, parent=subdivision
            )

        return None
