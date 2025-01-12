from django import forms
from .models import Patient
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class PatientRegistrationForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = [
            'first_name', 'last_name', 'gender',
            'phone_number', 'email', 'address',
            'city', 'state', 'zip_code'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            # 'date_of_birth': forms.DateInput(attrs={
            #     'type': 'date',
            #     'class': 'form-control',
            # }),
            'gender': forms.Select(attrs={
                'class': 'form-control'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@email.com'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address',
                'rows': 1
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'State'
            }),
            'zip_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Zip code'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        patient = super().save(commit=False)
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
        )
        patient.user = user  

        if commit:
            patient.save()
        return patient

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'autofocus': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        })
    )