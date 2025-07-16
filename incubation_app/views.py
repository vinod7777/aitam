from django.shortcuts import render, redirect
from .models import Submission

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company = request.POST.get('company')
        location = request.POST.get('location')
        join_as = request.POST.get('stage')
        Submission.objects.create(
            name=name,
            email=email,
            phone=phone,
            company=company,
            location=location,
            join_as=join_as
        )
        return render(request, 'index.html', {'success': True})
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def event(request):
    return render(request, 'event.html')

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')
