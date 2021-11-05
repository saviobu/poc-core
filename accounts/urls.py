from django.urls import path
from . import views

urlpatterns = [
    path('',views.NewAccount.as_view(), name='newaccount'),
    path('newtransaction/',views.NewTransaction.as_view(), name='newtransaction'),
    path('bulktransaction/',views.BulkTransaction.as_view(), name='bulktransaction'),
    path('listusertransactions/',views.ListUserTransactions.as_view(), name='listusertransactions'),
    path('transactionssummary/<id>',views.TransactionsSummary.as_view(), name='transactions_summary'),

]
