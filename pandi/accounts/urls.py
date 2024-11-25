from django.contrib import admin
from django.urls import path
from . import views
from .views import doctor_dashboard, patient_dashboard, patient_registration, CustomLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', patient_registration, name='patient_registration'),
    path('login/', CustomLoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('patient/dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
]