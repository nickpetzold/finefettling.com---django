from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

def landing(request):
    return render(request, 'members_area/landing.html')

def home(request):
    return render(request, 'members_area/home.html')

def garage(request):
    context = {
        'cars': Car.objects.all()
    }
    return render(request, 'members_area/garage.html', context)

def events(request):
    return render(request, 'members_area/events.html')

def pricing(request):
    return render(request, 'members_area/pricing.html')
