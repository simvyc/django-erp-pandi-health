from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm, PatientRegistrationForm
from accounts.models import Patient
from django.shortcuts import render, get_object_or_404
from .models import Patient

# Create your views here.

from django.shortcuts import render, redirect
from .forms import PatientRegistrationForm

def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success!!!")
    else:
        form = PatientRegistrationForm()
    return render(request, 'accounts/register_patient.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # Authenticate and log in the user
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                # Redirect to a success
                return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    return HttpResponse("This is LogOut")

def patient_profile(request):
    # Ensure the user is authenticated and linked to a patient profile
    if not request.user.is_authenticated:
        return redirect('login')

    # Retrieve the patient's profile linked to the logged-in user
    patient = get_object_or_404(Patient, user=request.user)

    # Render the profile page with patient details
    return render(request, 'patient_profile.html', {'patient': patient})