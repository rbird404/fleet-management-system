from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

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
from dashboard import services


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
        data = services.get_total_mileage(qs)
        serializer = self.get_serializer(data=data, many=True)
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
        data = services.get_vehicle_top_counters(qs)
        serializer = self.get_serializer(data=data, many=True)
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
        data = services.get_vehicle_top_fueling(qs)
        serializer = self.get_serializer(data=data, many=True)
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
        data = services.get_fuel_cost(qs)
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CostPerKilometerAPI(ListAPIView):
    """Стоимость километра пути"""
    queryset = Vehicle.objects.all()
    filterset_class = VehicleFilter
    serializer_class = CostPerKilometerSerializer
    my_tags = ['dashboard']

    def list(self, request, *args, **kwargs):
        date_after = request.query_params.get('date_after')
        date_before = request.query_params.get('date_before')
        qs = self.filter_queryset(self.get_queryset())
        data = services.get_cost_per_kilometer(qs, date_after, date_before)
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ExpensesCostAPI(ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpensesCostSerializer
    filterset_class = ExpenseFilter
    my_tags = ['dashboard']

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = services.get_expenses_cost(qs)
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ServiceCostAPI(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = ServiceCostSerializer
    filterset_class = RecordFilter
    my_tags = ['dashboard']

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        data = services.get_services_cost(qs)
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
