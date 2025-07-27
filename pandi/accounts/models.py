from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)
    address = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    is_active = models.BooleanField(default=True)
    is_patient = models.BooleanField(default=True, editable=False)

    family_doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True, blank=True, related_name='patients', verbose_name="Family Doctor"
    )
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
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
