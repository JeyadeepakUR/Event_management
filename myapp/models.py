from django.db import models
from django.contrib.auth.models import User

class UserProfile(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    netid = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pic', null = True, blank=True)
    password = models.CharField(max_length=100)
    Cpassword = models.CharField(max_length=100)
    pass