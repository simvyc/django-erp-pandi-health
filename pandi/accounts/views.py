from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Patient
from .forms import PatientRegistrationForm
from django.contrib.auth.decorators import login_required

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('profile_patient')
    else:
        form = PatientRegistrationForm()

    return render(request, 'accounts/register_patient.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                auth_login(request, user)

                if hasattr(user, 'doctor'):
                    return redirect('profile_doctor')
                elif hasattr(user, 'patient'):
                    return redirect('profile_patient')
                else:
                    return HttpResponse('No associated account type.')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    auth_logout(request)  
    return redirect('login')

def registration_successful(request):
    return render(request, 'accounts/registration_successful.html')

@login_required
def profile_patient(request):
    patient = get_object_or_404(Patient, user=request.user)
    return render(request, 'accounts/profile_patient.html', {'patient': patient})

@login_required
def profile_doctor(request):
    if hasattr(request.user, 'doctor'):
        doctor = request.user.doctor
        patients = doctor.patients.all()
    else:
        patients = []
    return render(request, 'accounts/profile_doctor.html', {'patients': patients})





