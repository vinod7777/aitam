from django.shortcuts import render

# Create your views here.

def final(request):
    return render(request, 'final.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')
