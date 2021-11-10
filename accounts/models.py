from django.db import models
from django.db.models.fields.related import ForeignKey
from users.models import User


class Account(models.Model):
    account_id = models.CharField(max_length=6, primary_key=True, unique=True, error_messages={'unique': "Account_ID already exists"})
    user_id = ForeignKey(User, on_delete=models.DO_NOTHING)
    balance = models.FloatField(default=0)


class Transaction(models.Model):
    reference = models.BigAutoField (unique=True, primary_key=True, error_messages={'unique': "Reference already exists"})
    account_id = ForeignKey(Account, on_delete=models.DO_NOTHING)
    date = models.DateField()
    amount = models.FloatField()
    type = models.CharField(max_length=7, choices=(('O', 'Outflow'),('I', 'Inflow')))
    category = models.CharField(max_length=20)
