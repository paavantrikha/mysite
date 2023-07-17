from django import forms
from django.contrib.auth.models import User #User is a built-in django model
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm): # Inherited UserCreationForm class to add our own fields while creating user
    email = forms.EmailField() # To add email to form while creating user

    class Meta: #Provides info about this class(RegisterForm). Meta - Data about data
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #password2 for confirmation
