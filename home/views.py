from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    return render(request, 'index.html')

def about(request):
    number=10
    return render(request, 'about.html', {'number':number})

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')