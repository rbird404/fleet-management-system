from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.db.models import Max, Sum, F, Q
from django.db.models.functions import TruncMonth, TruncYear

from common.filters import BaseFilterSet
from fueling.models import Fueling
from vehicles.models import Vehicle, Counter, Expense
from maintenance.models import Record, Issue
from fueling.filters import FuelingFilter
from vehicles.filters import CounterFilter
from dashboard.filters import (
    VehicleFilter, RecordFilter, ExpenseFilter
)
from dashboard.serializers import (
    VehicleCountSerializer, IssueCountSerializer, VehicleTopCounterSerializer,
    TotalMileageSerializer, VehicleTopFuelingSerializer, FuelCostSerializer,
    CostPerKilometerSerializer, ExpensesCostSerializer, ServiceCostSerializer
)


class VehicleCountAPI(ListAPIView):
    """Количество ТС"""
    queryset = Vehicle.objects.all()
    filterset_class = BaseFilterSet
    serializer_class = VehicleCountSerializer
    my_tags = ['dashboard']

    def list(self, request, *args, **kwargs):
        data = {
            'count': self.filter_queryset(self.get_queryset()).count()
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IssueCountAPI(ListAPIView):
    """Количество проблем"""
    queryset = Issue.objects.all()
    serializer_class = IssueCountSerializer
    my_tags = ['dashboard']

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = {
            'open': qs.filter(status='open').count(),
            'overdue': qs.filter(status='overdue').count()
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TotalMileageAPI(ListAPIView):
    """Общий пробег по автопарку"""
    queryset = Counter.objects.all()
    serializer_class = TotalMileageSerializer
    filterset_class = CounterFilter
    my_tags = ['dashboard']

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = qs.annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            counter=Max('value')
        ).values('month', 'counter')
        serializer = self.get_serializer(data=list(data), many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VehicleTopCounterAPI(ListAPIView):
    """Топ ТС по пробегу"""
    queryset = Counter.objects.all()
    serializer_class = VehicleTopCounterSerializer
    filterset_class = CounterFilter
    my_tags = ['dashboard']

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = qs.values(
            inv_number=F('vehicle__inventory_number')
        ).annotate(counter=Max('value'))
        serializer = self.get_serializer(data=list(data), many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VehicleTopFuelingAPI(ListAPIView):
    """Топ ТС по тратам на топливо"""
    queryset = Fueling.objects.all()
    serializer_class = VehicleTopFuelingSerializer
    filterset_class = FuelingFilter
    my_tags = ['dashboard']

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = qs.values(
            inv_number=F('vehicle__inventory_number')
        ).annotate(price=Sum('summ')).order_by('-price')
        serializer = self.get_serializer(data=list(data), many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FuelCostAPI(ListAPIView):
    """Затраты на топливо"""
    queryset = Fueling.objects.all()
    serializer_class = FuelCostSerializer
    filterset_class = FuelingFilter
    my_tags = ['dashboard']

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = qs.annotate(
            month=TruncMonth('date')
        ).values('month').annotate(cost=Sum('summ')).values('month', 'cost')
        serializer = self.get_serializer(data=list(data), many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CostPerKilometerAPI(ListAPIView):
    """Стоимость километра пути"""
    queryset = Vehicle.objects.all()
    filterset_class = VehicleFilter
    serializer_class = CostPerKilometerSerializer
    my_tags = ['dashboard']

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = qs.annotate(
            month=TruncMonth('fueling__date'),
            year_=TruncYear('fueling__date'),
            price=Sum(F("fueling__summ")) / Max(F("counters__value"))
        ).exclude(
            Q(month=None) | Q(price=None)
        ).values('month', 'price')
        # TODO добавить учет доп расходов
        # expenses = qs.annotate(
        #     month=TruncMonth('expenses__date'),
        #     price=Sum(F("expenses__price")) / Max(F("counters__value"))
        # ).values('month', 'price')

        serializer = self.get_serializer(data=list(data), many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExpensesCostAPI(ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpensesCostSerializer
    filterset_class = ExpenseFilter
    my_tags = ['dashboard']

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = qs.annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            price=Sum('price')
        ).values('month', 'price')
        serializer = self.get_serializer(data=list(data), many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ServiceCostAPI(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = ServiceCostSerializer
    filterset_class = RecordFilter
    my_tags = ['dashboard']

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = qs.annotate(
            month=TruncMonth('start_date')
        ).values('month').annotate(
            price=Sum('price')
        ).values('month', 'price')
        serializer = self.get_serializer(data=list(data), many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
