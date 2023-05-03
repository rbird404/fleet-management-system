from common.views import APIViewSet
from expenses.models import Expense, ExpenseType

from expenses.serializers import ExpenseSerializer, ExpenseTypeSerializer


class ExpenseViewSet(APIViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseTypeViewSet(APIViewSet):
    queryset = ExpenseType.objects.all()
    serializer_class = ExpenseTypeSerializer
