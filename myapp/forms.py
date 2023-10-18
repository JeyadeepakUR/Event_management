from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=[('student', 'Student'), ('faculty', 'Faculty')], widget=forms.RadioSelect, label='UserType')
    class Meta:
        model = UserProfile
        fields = ['username', 'netId', 'Ph.No', 'Dept', 'password', 'Cpassword', 'user_type']
        
class Loginform(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']
    

class SponsorLoginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'Cpassword', 'Ph.No', 'Email']