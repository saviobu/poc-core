from django.http.response import HttpResponse
from django.views.generic.list import ListView
from django.views import View
from .usersservices import UsersServices


class UserList(ListView):
    def get(self, *args, **kwargs):
        try:
            response = UsersServices.all_users()
            return HttpResponse(response)
        
        except ValueError as exp:
            return HttpResponse(f'Error listing all users ! Error: {exp}'), 500



class UserDetails(View):
    def get(self, *args, **kwargs):
        try:
            response = UsersServices.user_details(kwargs.get('id'))
            return HttpResponse(response)
        except ValueError as exp:
            return HttpResponse(f'User not found ! Error: {exp}'), 500



class NewUser(View):
    def post(self,*args, **kwargs):
        try:
            response = UsersServices.new_user(self.request)
            return HttpResponse(response)
        except ValueError as exp:
            return HttpResponse(f'Error creating user ! Error: {exp}'), 500
