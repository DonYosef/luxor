from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, '../templates/home.html')

def login(request):
    return render(request, '../templates/login.html')

def register(request):
    return render(request, '../templates/register.html')

def profile(request):
    return render(request, '../templates/profile.html')

def table(request):
    return render(request, '../templates/table.html')

