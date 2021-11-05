from django.db import models
from rest_framework import serializers


class User(models.Model):
    user_id = models.BigAutoField (unique=True, primary_key=True, error_messages={'unique': "User_id already exists"})
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    age = models.IntegerField(blank=True)

    def __str__(self):
        return f'User_Id: {self.user_id},  Name: {self.name},  Email: {self.email}, Age: {self.age}\n'


class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__All__'
