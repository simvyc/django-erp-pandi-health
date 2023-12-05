from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def orders_list(request):
    
    return render(request, 'templates/orders_list.html')
