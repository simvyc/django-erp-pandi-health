from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from .forms import PatientRegistrationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from accounts.models import Patient, Doctor
from django.contrib.auth.decorators import login_required

# Create your views here.

# def register(request):
#     return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return HttpResponse("This is LogOut")

def patient_registration(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to a success page
    else:
        form = PatientRegistrationForm()
    return render(request, 'accounts/patient_registration.html', {'form': form})

class CustomLoginView(LoginView):
    def get_success_url(self):
        if hasattr(self.request.user, 'patient_profile'):
            return reverse('patient_dashboard')  # Redirect to the patient dashboard
        elif hasattr(self.request.user, 'doctor_profile'):
            return reverse('doctor_dashboard')  # Redirect to the doctor dashboard
        return reverse('home')
    
@login_required
def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html')