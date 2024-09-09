from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')  

def about(request):
    return render(request, 'navbar/about.html') 

def service(request):
    return render(request, 'navbar/service.html') 

def contact(request):
    return render(request, 'navbar/contact.html') 
# def home(request):
#     return HttpResponse("This is home")