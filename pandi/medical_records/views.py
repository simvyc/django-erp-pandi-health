from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def records(request):
    return render(request, 'records.html')

def prescriptions(request):
    return HttpResponse('This is prescriptions list.')

