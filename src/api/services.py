from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, QuerySet
from django.db.models import Q

from api.exceptions import FieldNotAllowed
from cars.models import Car
from history.models import History


class HistoryService:
    allowed_fields: list[str] = (
        "type",
        "manufacturer",
        "brand",
        "body",
        "group",
        "chass_number",
        "body_number",
        "year",
        "passport",
        "gov_number",
        "register_number",
        "sign_date",
        "exploitation_date",
        "car_class",
        "color",
        "service",
        "subdivision",
        "cost",
        "source",
        "source_number",
        "source_date",
        "warehouse",
        "waybill",
        "distribution",
        "transfer_date",
        "del_date",
        "mileage_rate",
        "fuel_rate",
        "id_number",
        "gasoline_brand",
        "engine",
        "climate_control",
        "base_rate",
        "identifier_fuel_rate",
        "category",
        "trust_date",
        "to_date",
    )

    def __init__(self, car: Car):
        self.car = car

    def get_history_by_field(self, field: str) -> QuerySet[History]:
        if field not in self.allowed_fields:
            raise FieldNotAllowed(field=field)

        value = getattr(self.car, field)

        if isinstance(value, Model):
            qs = History.objects.filter(
                content_type=ContentType.objects.get_for_model(value),
                object_id=value.id
            )
        else:
            qs = History.objects.filter(
                content_type=ContentType.objects.get_for_model(Car),
                object_id=self.car.id, field=field
            )

        return qs

    def get_all_history(self) -> QuerySet[History]:
        query = Q(
            content_type=ContentType.objects.get_for_model(Car),
            object_id=self.car.id
        )

        for field in ('engine', 'waybill', 'distribution', 'passport'):
            if obj := getattr(self.car, field):
                query |= Q(
                    content_type=ContentType.objects.get_for_model(obj),
                    object_id=obj.id
                )

        return History.objects.filter(query)

    def get_history(self, field: str | None) -> QuerySet[History]:
        if field is None:
            return self.get_all_history()
        return self.get_history_by_field(field)
