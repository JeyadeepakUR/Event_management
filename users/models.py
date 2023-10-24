from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CustomUser(AbstractUser):
    STATUS = {
        ('stu', 'Student'),
        ('fac', 'Faculty'),
        ('spo', 'Sponsor')
    }

    ORG_REQ = {
        ('req', 'Request'),
        ('pend', 'Pending'),
        ('appr', 'Approved'),
        ('den', 'Denied')
    }

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=50, choices=STATUS, blank=False)
    register_number = models.CharField(max_length=15, unique=True, blank=False)
    phone_number = PhoneNumberField(blank=False, null=False)
    is_organizer = models.BooleanField(default=False)
    org_req = models.CharField(max_length=15, choices=ORG_REQ, blank=True, default='req')
    club = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username
    