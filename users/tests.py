from django.test import TestCase, Client
from users.models import User
from django.urls import reverse

class UsersQueryDatabaseTests(TestCase):
    def setUp(self):
        User.objects.create(name="Joao", email="jj@gmail.com", age=34)
        User.objects.create(name="Ricardo", email="ric@gmail.com", age=40)
        User.objects.create(name="Fernando", email="fernando@bol.com", age=64)


    def test_list_all_users(self):
        all_users_response = User.objects.all()
        self.assertEqual(len(all_users_response), 3)
    

    def test_list_especific_user(self):
        especific_user_response = User.objects.filter(user_id = 2).first()
        self.assertEqual(str(especific_user_response),'User_Id: 2,  Name: Ricardo,  Email: ric@gmail.com, Age: 40\n')



class UsersConsumeEndpointTests(TestCase):
    def test_add_new_user_endpoint(self):
        self.client = Client()
        new_user = reverse('newuser')
        register_1 = {'name': 'Alfredo', 'email': 'alf.rgs@hotmail.com.com', 'age': 84}
        register_2 = {'name': 'Pedro Alves', 'email': 'pedro@gmail.com', 'age': 14}
        response = self.client.post(new_user, register_1, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.client.post(new_user, register_2, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        

    def test_list_all_users_from_endpoits(self):
        userlist = reverse('userlist')
        all_users_response = self.client.get(userlist)
        self.assertEqual(all_users_response.status_code, 200)
    
    
    def test_list_especific_user_from_endpoint(self):
        userdetails = reverse('userlist')
        especific_user_response = self.client.get(userdetails+'1')
        self.assertEqual(especific_user_response.status_code, 200)