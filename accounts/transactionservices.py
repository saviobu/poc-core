from datetime import datetime
from .models import Transaction, Account
from .serializers import TransactionSerializer, ListTransactionSerializer
from django.db.models import Sum
from itertools import chain


class TransactionServices:

    @staticmethod
    def list_user_transactions (request):
        try:
            data = ListTransactionSerializer.data(request.body)
            id = data.get('user_id')
            initial_date = data.get('initial_date')
            final_date = data.get('final_date')
            
            if not final_date:
                final_date = datetime.now()
            
            if not initial_date:
                initial_date = datetime(1900,1,1)
                
            model = Transaction.objects.select_related('account_id').filter(account_id__user_id = int(id))\
                .values('reference','account_id','date','amount','type','category','account_id__user_id')

            sumary_inflow = Transaction.objects.select_related('account_id').filter(account_id__user_id = int(id)).filter(type='Inflow')\
                .values('account_id','account_id__balance').order_by('type').annotate(Total_Inflow = Sum('amount'))

            sumary_outflow = Transaction.objects.select_related('account_id').filter(account_id__user_id = int(id)).filter(type='Outflow')\
                .values('account_id','account_id__balance').annotate(Total_Outflow = Sum('amount'))
            
            response = list(chain(model,sumary_inflow,sumary_outflow))
            
            return response

        except ValueError as exc:
            return exc


    @staticmethod
    def transactions_summary (id):
        try:
            
            response = Transaction.objects.select_related('account_id').filter(account_id__user_id = int(id))\
                    .values('category','type').annotate(Total = Sum('amount')).order_by('-type')

            list = {'Inflow':[],'Outflow':[]}

            for valores in response:
                if valores['type'] == 'Inflow':
                    list['Inflow'].append([valores['category'], valores['Total']])
                
                elif valores['type'] == 'Outflow':
                    list['Outflow'].append([valores['category'], valores['Total']])
            list['Inflow'] = dict(list['Inflow'])
            list['Outflow'] = dict(list['Outflow'])
            response = str(list)

            return response

        except ValueError as exc:
            return exc
    

    @staticmethod
    def bulk_transactions(request):
        cont = 1
        try:
                
            block = list(TransactionSerializer.data(request.body))
            for data in block:
                AddTransactions.add_transactions(data)
                cont += 1

            return f'Success, {cont} transactions inserted !'
        
        except ValueError as exc:
            return exc


class AddTransactions:

    @staticmethod
    def add_transactions(data):
        try:
        
            _account_id = data.get('account_id')
            _amount = float(data.get('amount'))
            account_info = Account.objects.filter(account_id = _account_id).first()
            new_balance = float(account_info.balance) + _amount
            Account.objects.filter(account_id = _account_id).update(balance = new_balance)
            _category = data.get('category')
            _date = datetime.now()
            _type = 'Inflow'
            if _amount < 0:
                _type = 'Outflow'
            Transaction.objects.create(account_id = account_info, amount = _amount, type = _type, date = _date, category = _category)
        
        except ValueError as exc:
            return exc      
  