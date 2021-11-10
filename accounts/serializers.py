from .models import Account, Transaction
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account 
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class ListTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('user_id', 'initial_date', 'final_date')
