from common.serializers import BaseSerializer
from expenses.models import Expense, ExpenseType


class ExpenseTypeSerializer(BaseSerializer):
    class Meta:
        model = ExpenseType
        fields = "__all__"


class ExpenseSerializer(BaseSerializer):
    class Meta:
        model = Expense
