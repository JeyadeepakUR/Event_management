from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'Cpassword', 'netid', 'phone']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']