from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    # path('', views.base, name='base'),
    path('', views.records, name='records'),
    path('prescriptions/', views.prescriptions, name='prescriptions'),
]
