from django.contrib import admin
from django.urls import path
from . import views
from .views import patient_profile, register_patient, login, logout


urlpatterns = [
    path('register_patient/', register_patient, name='register_patient'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('patient_profile/', patient_profile, name='profile_patient'),
    # path('doctor_profile/', doctor_profile, name='profile_doctor'),
]