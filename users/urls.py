from django.urls import path
from . import views

urlpatterns = [
    path('',views.UserList.as_view(), name='userlist'),
    path('<id>',views.UserDetails.as_view(), name='userdetails'),
    path('newuser/',views.NewUser.as_view(), name='newuser'),
]
