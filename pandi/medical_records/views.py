from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def records(request):
    return render(request, 'records.html')

# def records(request):
#      return HttpResponse('This is records list.')

def prescriptions(request):
    return HttpResponse('This is prescriptions list.')



