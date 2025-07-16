from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request, 'landing.html')

def startup(request):
    return render(request, 'startup.html')

def team(request):
    return render(request, 'team.html')

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')
