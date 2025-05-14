from django import forms
from .models import Patient
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()

class PatientRegistrationForm(forms.ModelForm):
    # Fields from CustomUser
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}),
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
    )

    class Meta:
        model = Patient
        fields = []  # No model-specific fields from Patient

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', "A user with this email already exists.")

        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data.get('email'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
        )
        user.phone_number = self.cleaned_data.get('phone_number')
       
        if commit:
            user.save()

        patient = super().save(commit=False)
        patient.user = user
        if commit:
            patient.save()

        return patient

class LoginForm(AuthenticationForm):

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
   
            'placeholder': 'Username',
            'autofocus': True,
            'autocomplete': 'username',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
   
            'placeholder': 'Password',
            'autocomplete': 'current-password',
        })
    )
from django import forms
from .models import Appointment



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'date', 'time', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
