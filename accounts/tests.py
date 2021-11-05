from django.test import TestCase, Client
from users.models import User
from accounts.models import Account
from django.urls import reverse


class AccountDatabaseTests(TestCase):
    def setUp(self):
        User.objects.create(name="Joao", email="jj@gmail.com", age=34)
        user_instance = User.objects.filter(user_id = 1).first()
        Account.objects.create(account_id = 'S00001', user_id = user_instance)

        User.objects.create(name="Ricardo", email="ric@gmail.com", age=40)
        user_instance = User.objects.filter(user_id = 2).first()
        Account.objects.create(account_id = 'S00002', user_id = user_instance)



    def test_new_transaction_endpoit(self):
        self.client = Client()
        transactions_endpoint = reverse('newtransaction')

        transaction = {'account_id': 'S00001', 'amount': 10.20, 'category':'Bonus' }
        response = self.client.post(transactions_endpoint, data=transaction, content_type='application/json')
        self.assertEqual(response.status_code,200)
        
        transaction = {'account_id': 'S00001', 'amount': 20.30, 'category':'Bonus' }
        response = self.client.post(transactions_endpoint, data=transaction, content_type='application/json')
        self.assertEqual(response.status_code,200)
        
        transaction = {'account_id': 'S00002', 'amount': 10.20, 'category':'Bonus' }
        response = self.client.post(transactions_endpoint, data=transaction, content_type='application/json')
        self.assertEqual(response.status_code,200)

        transaction = {'account_id': 'S00002', 'amount': 40.40, 'category':'Bonus' }
        response = self.client.post(transactions_endpoint, data=transaction, content_type='application/json')
        self.assertEqual(response.status_code,200)


    def test_new_transaction_database_direct(self):
        result = Account.objects.filter(account_id = 'S00001').values('balance').first()
        self.assertEqual(result.get('balance'),30.50)
        result = Account.objects.filter(account_id = 'S00002').values('balance').first()
        self.assertEqual(result.get('balance'),50.60)


    def test_list_user_transactions_endpoint(self):
        list_transactions_endpoint = reverse('listusertransactions')
        filter = {'user_id': 1}
        response = self.client.post(list_transactions_endpoint, filter, content_type='application/json')
        self.assertEqual(response.status_code,200)

    
    def test_list_user_TransactionsSummary_endpoint(self):
        list_transactions_endpoint = reverse('transactions_summary')
        response = self.client.get(list_transactions_endpoint+'1')
        self.assertEqual(response.status_code,200)
    

    def test_bulk_transactions(self):
        transactions_endpoint = reverse('bulktransaction')

        transaction = [{'account_id': 'S00001', 'amount': 100.00, 'category':'Bonus' },{'account_id': 'S00001', 'amount': -50.00, 'category':'Taxes' },\
            {'account_id': 'S00002', 'amount': 150.00, 'category':'Bonus' },{'account_id': 'S00002', 'amount': -100.20, 'category':'Taxes' }, ]
        response = self.client.post(transactions_endpoint, data=transaction, content_type='application/json')
        self.assertEqual(response.status_code,200)
