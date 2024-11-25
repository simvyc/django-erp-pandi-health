from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Patient

class PatientRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    city = forms.CharField(max_length=25, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'city', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = False  # Ensure the user is not staff
        user.is_superuser = False  # Ensure the user is not a superadmin
        if commit:
            user.save()
            # Create associated Patient profile
            Patient.objects.create(
                user=user,
            )
        return user
