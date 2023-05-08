from django.db.models import Max, Sum, F
from django.db.models.functions import TruncMonth, TruncYear
from rest_framework import status
from rest_framework.generics import ListAPIView

from common.filters import BaseFilterSet
from dashboard.serializers import VehicleCountSerializer, IssueCountSerializer, VehicleTopCounterSerializer, \
    TotalMileageSerializer, VehicleTopFuelingSerializer, FuelCostSerializer, CostPerKilometerSerializer
from fueling.models import Fueling
from vehicles.models import *
from maintenance.models import *
from rest_framework.response import Response
from fueling.filters import FuelingFilter
from vehicles.filters import CounterFilter

from dashboard.filters import VehicleFilter


class VehicleCountAPI(ListAPIView):
    """Количество ТС"""
    queryset = Vehicle.objects.all()
    filterset_class = BaseFilterSet
    serializer_class = VehicleCountSerializer

    def list(self, request, *args, **kwargs):
        data = {
            'count': self.filter_queryset(self.get_queryset()).count()
        }
        return Response(data, status=status.HTTP_200_OK)


class IssueCountAPI(ListAPIView):
    """Количество проблем"""
    queryset = Issue.objects.all()
    serializer_class = IssueCountSerializer

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = {
            'open': qs.filter(status='open').count(),
            'overdue': qs.filter(status='overdue').count()
        }
        return Response(data, status=status.HTTP_200_OK)


class TotalMileageAPI(ListAPIView):
    """Общий пробег по автопарку"""
    queryset = Counter.objects.all()
    serializer_class = TotalMileageSerializer
    filterset_class = CounterFilter

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = qs.annotate(
            month=TruncMonth('date')
        ).values('month').annotate(counter=Max('value')).values(
            'month', 'counter'
        )
        return Response(data, status=status.HTTP_200_OK)


class VehicleTopCounterAPI(ListAPIView):
    """Топ ТС по пробегу"""
    queryset = Counter.objects.all()
    serializer_class = VehicleTopCounterSerializer
    filterset_class = CounterFilter

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = qs.values(
            inv_number=F('vehicle__inventory_number')
        ).annotate(counter=Max('value'))
        return Response(data, status=status.HTTP_200_OK)


class VehicleTopFuelingAPI(ListAPIView):
    """Топ ТС по тратам на топливо"""
    queryset = Fueling.objects.all()
    serializer_class = VehicleTopFuelingSerializer
    filterset_class = FuelingFilter

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = qs.values(
            inv_number=F('vehicle__inventory_number')
        ).annotate(price=Sum('summ')).order_by('-price')
        return Response(data, status=status.HTTP_200_OK)


class FuelCostAPI(ListAPIView):
    """Затраты на топливо"""
    queryset = Fueling.objects.all()
    serializer_class = FuelCostSerializer
    filterset_class = FuelingFilter

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = qs.annotate(
            month=TruncMonth('date')
        ).values('month').annotate(cost=Sum('summ')).values('month', 'cost')
        return Response(data, status=status.HTTP_200_OK)


class CostPerKilometerAPI(ListAPIView):
    """Стоимость километра пути"""
    queryset = Vehicle.objects.all()
    filterset_class = VehicleFilter
    serializer_class = CostPerKilometerSerializer

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())

        fueling = qs.annotate(
            month=TruncMonth('fueling__date'),
            year_=TruncYear('fueling__date'),
            price=Sum(F("fueling__summ")) / Max(F("counters__value"))
        ).values('month', 'price')

        # expenses = qs.annotate(
        #     month=TruncMonth('expenses__date'),
        #     price=Sum(F("expenses__price")) / Max(F("counters__value"))
        # ).values('month', 'price')

        return Response(fueling, status=status.HTTP_200_OK)


# class ExpensesCostAPI(ListAPIView):
#     queryset = Expense.objects.all()
#
#     def list(self, request, *args, **kwargs):
#         qs = self.filter_queryset(self.get_queryset())
#
