from django.contrib import admin
from django.urls import path
from .views import profile_patient, profile_doctor, register_patient, login, logout, registration_successful


urlpatterns = [
    path('register_patient/', register_patient, name='register_patient'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registration_successful/', registration_successful, name='registration_successful'),
    path('profile_patient/', profile_patient, name='profile_patient'),
    path('profile_doctor/', profile_doctor, name='profile_doctor'),
]