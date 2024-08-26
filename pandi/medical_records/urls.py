from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('records/', views.records, name='records'),
    path('prescriptions/', views.prescriptions, name='prescriptions'),
]
