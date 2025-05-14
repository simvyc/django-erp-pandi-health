from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  

def about(request):
    return render(request, 'navbar/about.html') 

def contact(request):
    return render(request, 'navbar/contact.html') 

from accounts.models import Doctor

def about(request):
    doctors = Doctor.objects.all()
    return render(request, "navbar/about.html", {"doctors": doctors})