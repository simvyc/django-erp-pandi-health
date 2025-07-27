# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Patient

class PatientRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], required=False)
    address = forms.CharField(max_length=80, required=False)
    city = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=100, required=False)
    zip_code = forms.CharField(max_length=10, required=False)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth',
            'gender', 'address', 'city', 'state', 'zip_code', 'password1', 'password2',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email  
        user.is_active = True
        if commit:
            user.save()
            Patient.objects.create(user=user) 
        return user
