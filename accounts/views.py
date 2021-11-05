from django.http.response import HttpResponse
from django.views.generic.list import ListView
from django.views import View
from accountservices import AccountAction
from transactionservices import AddTransactions, TransactionActions


class NewTransaction(View):
    def post(self, *args, **kwargs):
        try:
            AddTransactions.add_transactions(self.request)
            return HttpResponse(f'Success !')            
        
        except ValueError as exc:
            return HttpResponse(f'Error {exc}!'), 500                    


class BulkTransaction(View):
    def post(self, *args, **kwargs):
        try:
            response = TransactionActions.bulk_transactions(self.request)
            return HttpResponse(response)            
        
        except ValueError as exc:
            return HttpResponse(f'Error {exc}!'), 500


class NewAccount(View):
    def post(self, *args, **kwargs):
        try:
            response = AccountAction.new_account(self.request)
            return HttpResponse(response)            
        
        except ValueError as exc:
            return HttpResponse(f'Error {exc}!'), 500                    


class ListUserTransactions(ListView):
    def post (self, *args, **kwargs):
        try:
            response = TransactionActions.list_user_transactions(self.request)            
            return HttpResponse(response) 

        except ValueError as exc:
            return HttpResponse(f'Error {exc} !'), 400


class TransactionsSummary(ListView):
    def get (self, *args, **kwargs):
        try:
            response = TransactionActions.transactions_summary (id)
            return HttpResponse(response) 
        except ValueError as exc:
            return HttpResponse(f'Error {exc} !'), 400
