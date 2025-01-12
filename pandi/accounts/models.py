from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    # date_of_birth = models.TextField(max_length=15, null=True)
    gender = models.TextField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    phone_number = models.CharField(max_length=15, null=True)
    email = models.EmailField(unique=True, blank=True)
    address = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    # registration_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_patient = models.BooleanField(default=True, editable=False)

    family_doctor = models.ForeignKey(
        'Doctor',  # Ref. to the Doctor model
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='patients',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True)
    email = models.EmailField(unique=True, blank=True)
    residence_address = models.CharField(max_length=100, blank=True)
    registration_address = models.CharField(max_length=100, blank=True)
    room_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20, unique=True)
    allergies = models.TextField(blank=True, null=True)
    contact_person_name = models.CharField(max_length=100)
    contact_person_phone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialty}"
    
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"