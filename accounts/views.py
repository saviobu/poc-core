from rest_framework.viewsets import ModelViewSet
from .models import Account, Transaction
from .models import Transaction, Account
from .serializers import TransactionSerializer, AccountSerializer
from .transactionservices import TransactionServices



class AccountsViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransactionsViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


    def bulk_transaction(self):
        self.queryset.bulk_create(self.request.POST)


    def list_user_transactions (self):
        serializer_class = TransactionServices.list_user_transactions(self.request.POST)


    def transactions_summary (self, *args, **kwargs):
        response = TransactionServices.transactions_summary (id)
