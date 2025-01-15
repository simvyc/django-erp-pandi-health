from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from .forms import PatientRegistrationForm
from accounts.models import Patient
from django.shortcuts import render, get_object_or_404
from .models import Doctor, Patient
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings

User = get_user_model()

# Create your views here.

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_successful')
    else:
        form = PatientRegistrationForm()
    return render(request, 'accounts/register_patient.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if hasattr(user, 'profile_doctor'):
                    return render(request, 'accounts/profile_doctor.html')  
                elif hasattr(user, 'profile_patient'):
                    return render(request, 'accounts/profile_patient.html') 
                else:
                    return HttpResponse('Ner tokio acc') 
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    return HttpResponse("This is LogOut")

def registration_successful(request):
    return render(request, 'accounts/registration_successful.html')

def profile_patient(request):
    if not request.user.is_authenticated:
        return redirect('login')
    patient = get_object_or_404(Patient, user=request.user)
    return render(request, 'profile_patient.html', {'patient': patient})

def profile_doctor(request):
    if not request.user.is_authenticated:
        return redirect('login')
    doctor = get_object_or_404(Doctor, user=request.user)
    return render(request, 'profile_doctor.html', {'doctor': doctor})