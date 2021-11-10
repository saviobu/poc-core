from rest_framework.viewsets import ModelViewSet
from .models import Account, Transaction
from .models import Transaction, Account
from .serializers import TransactionSerializer, AccountSerializer


class AccountsViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransactionsViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
