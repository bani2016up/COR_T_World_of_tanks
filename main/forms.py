from dataclasses import field
from statistics import mode
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        mode = User
        fields = ['username', 'email', 'password1', 'password2']