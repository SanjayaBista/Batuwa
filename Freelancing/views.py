from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from .models import *
# Create your views here.
def home(request):
    return render(request, 'index.html')

def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect("Freelancing:home")
        else:
            # messages.warning(request, "Username or Password is incorrect")
            return redirect("Freelancing:login")
 
    else:
        return render (request, 'login.html', {})
 

def userRegister(request):
    return render(request, 'register.html')