from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    # Custom fields
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)

    # Add explicit related_name arguments to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True
    )

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    gender = models.CharField(max_length=8) 
    allergies = models.CharField(max_length=50)
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialty = models.CharField(max_length=50)
    license_number = models.CharField(max_length=20)