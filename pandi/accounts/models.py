from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    state = models.CharField(max_length=100, default='Unknown')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.TextField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    phone_number = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='patient')
    is_active = models.BooleanField(default=True)
    is_patient = models.BooleanField(default=True, editable=False)
    contact_person_name = models.CharField(max_length=100)
    contact_person_phone = models.CharField(max_length=15)

    family_doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True, blank=True, related_name='patients', verbose_name="doctor"
    )
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
    
class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='doctor')
    room_name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20, unique=True)
    contact_person_name = models.CharField(max_length=100)
    contact_person_phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=True, editable=False)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name} - {self.speciality}" 

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient_name} on {self.date} at {self.time}"
