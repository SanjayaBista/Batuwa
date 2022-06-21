from importlib.util import decode_source
from multiprocessing import context
from pydoc import doc
from this import d
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, CreateView

from .forms import PostProjectForm

# from .forms import PostProjectForm  
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

def postProject(request):
    if request.method == 'POST':
        projectForm = PostProjectForm(request.POST, request.FILES)
        if projectForm.is_valid():
                
            projectForm.save()
            return redirect('Freelancing:viewProject')
        else:
            messages.error(request, "Error")
    else:
        projectForm = PostProjectForm()
    return render(request, 'postProject.html',{'projectForm':projectForm })


def viewProject(request):
    allProject = ProjectDetail.objects.all()
    context = {
        'allProject':allProject
    }
    return render(request, 'projectDetail.html', context)

def viewProjectDetail(request,id):
    project = ProjectDetail.objects.get(id=id)
    context = {
        'project':project
    }
    return render(request, 'viewProjectDetail.html', context)
# class PostProject(CreateView):
#     pass