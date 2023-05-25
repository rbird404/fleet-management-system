import datetime
from typing import Type

from django.db.models import Max, F, Sum, Q
from django.db.models.functions import TruncMonth

from fueling.models import Fueling
from maintenance.models import Record
from vehicles.models import Expense, Counter, Vehicle
from common.models import ActiveModelQuerySet


def get_total_mileage(qs: ActiveModelQuerySet[Counter]) -> list[dict]:
    """Общий пробег по автопарку"""
    data = qs.annotate(
        month=TruncMonth('date')
    ).values('month').annotate(
        counter=Max('value')
    ).values('month', 'counter')
    return list(data)


def get_vehicle_top_counters(qs: ActiveModelQuerySet[Counter]) -> list[dict]:
    """Топ ТС по пробегу"""
    data = qs.values(
        inv_number=F('vehicle__inventory_number')
    ).annotate(counter=Max('value'))
    return list(data)


def get_vehicle_top_fueling(qs: ActiveModelQuerySet[Counter]) -> list[dict]:
    data = qs.values(
        inv_number=F('vehicle__inventory_number')
    ).annotate(price=Sum('summ')).order_by('-price')
    return list(data)


def get_fuel_cost(qs: ActiveModelQuerySet[Fueling]) -> list[dict]:
    """Затраты на топливо"""
    data = qs.annotate(
        month=TruncMonth('date')
    ).values('month').annotate(cost=Sum('summ')).values('month', 'cost')
    return list(data)


class Data:
    def __init__(self, month, price):
        self.month = month
        self.price = price

    def __eq__(self, other):
        return self.month == other.month

    def __gt__(self, other):
        return self.month > other.month

    def __lt__(self, other):
        return self.month < other.month

    def __str__(self):
        return f"{self.month} {self.price}"

    def __repr__(self):
        return f"{self.month} {self.price}"

    def to_dict(self):
        return {
            "month": self.month,
            "price": self.price
        }


def cost_per_kilometer_filter(
        model: Type[Fueling] | Type[Record] | Type[Expense],
        date_field: str,
        price_field: str,
        vehicles: list[int],
        date_before: datetime.datetime | None = None,
        date_after: datetime.datetime | None = None,
) -> ActiveModelQuerySet[Fueling | Record | Expense]:

    query = model.objects.annotate(
        month=TruncMonth(date_field)
    ).values("month")

    if date_before is not None:
        query = query.annotate(
            price=Sum(price_field) / Max(
                "vehicle__counters__value",
                filter=Q(vehicle__counters__date__lte=date_before))
        ).filter(**{f"{date_field}__lte": date_before})
    else:
        query = query.annotate(
            price=Sum(price_field) / Max("vehicle__counters__value")
        )

    if date_after is not None:
        query = query.filter(**{f"{date_field}__gte": date_after})

    query = query.values('month', 'price').filter(
            vehicle__id__in=vehicles
    ).exclude(price=None)

    return query


def get_cost_per_kilometer(
        qs: ActiveModelQuerySet[Vehicle],
        date_before: datetime.datetime | None = None,
        date_after: datetime.datetime | None = None,
) -> list[dict]:
    """Стоимость километра пути"""
    vehicles: list[int] = qs.values_list("id", flat=True)

    fueling_query = cost_per_kilometer_filter(Fueling, "date", "summ", vehicles, date_after, date_before)
    expense_query = cost_per_kilometer_filter(Expense, "date", "price", vehicles, date_after, date_before)
    record_query = cost_per_kilometer_filter(Record, "end_date", "price", vehicles, date_after, date_before)

    data_union = [
        Data(
            month=item['month'],
            price=item['price']
        )
        for item in record_query.union(expense_query).union(fueling_query)
    ]
    result = []
    for data in data_union:
        if data in result:
            index = result.index(data)
            result[index].price += data.price
        else:
            result.append(data)
    result.sort()
    return [data.to_dict() for data in result]


def get_expenses_cost(qs: ActiveModelQuerySet[Expense]) -> list[dict]:
    """Затраты на Доп расходы"""
    data = qs.annotate(
        month=TruncMonth('date')
    ).values('month').annotate(
        price=Sum('price')
    ).values('month', 'price')
    return list(data)


def get_services_cost(qs: ActiveModelQuerySet[Record]) -> list[dict]:
    """Затраты на сервис"""
    data = qs.annotate(
        month=TruncMonth('end_date')
    ).values('month').annotate(
        price=Sum('price')
    ).values('month', 'price')
    return list(data)
