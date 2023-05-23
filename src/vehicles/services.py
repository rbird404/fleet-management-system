from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, QuerySet
from django.db.models import Q

from vehicles.exceptions import FieldNotAllowed
from vehicles.models import Vehicle
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
        "vehicle_class",
        "color",
        "service",
        "subdivision",
        "cost",
        "source",
        "source_number",
        "source_date",
        "warehouse",
        "distribution",
        "transfer_date",
        "del_date",
        "mileage_rate",
        "fuel_rate",
        "id_number",
        "fuel_type",
        "engine",
        "climate_control",
        "base_rate",
        "identifier_fuel_rate",
        "category",
        "trust_date",
        "to_date",
    )

    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def get_history_by_field(self, field: str) -> QuerySet[History]:
        if field not in self.allowed_fields:
            raise FieldNotAllowed(field=field)

        value = getattr(self.vehicle, field)

        if isinstance(value, Model):
            qs = History.objects.filter(
                content_type=ContentType.objects.get_for_model(value),
                object_id=value.id
            )
        else:
            qs = History.objects.filter(
                content_type=ContentType.objects.get_for_model(Vehicle),
                object_id=self.vehicle.id, field=field
            )

        return qs

    def get_all_history(self) -> QuerySet[History]:
        query = Q(
            content_type=ContentType.objects.get_for_model(Vehicle),
            object_id=self.vehicle.id
        )

        for field in ('engine', 'distribution', 'passport'):
            if obj := getattr(self.vehicle, field):
                query |= Q(
                    content_type=ContentType.objects.get_for_model(obj),
                    object_id=obj.id
                )

        return History.objects.filter(query)

    def get_history(self, field: str | None) -> QuerySet[History]:
        if field is None:
            return self.get_all_history()
        return self.get_history_by_field(field)
