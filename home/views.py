from django.http import HttpResponse
from django.shortcuts import redirect, render

def home(request):

    return render(request, 'index.html')

def about(request):
    number=10
    return render(request, 'about.html', {'number':number})

def contact(request):
    return render(request, 'contact.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if email == "admin@gmail.com" and password == "1234":
            return redirect('home')
    return render(request, 'login.html')