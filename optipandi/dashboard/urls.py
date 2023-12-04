# dashboard/urls.py
from django.urls import path
from .views import dashboard
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
]
