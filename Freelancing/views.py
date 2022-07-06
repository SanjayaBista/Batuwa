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

def user_login(request):
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
 

def user_register(request):
    return render(request, 'register.html')

def post_project(request):
    if request.method == 'POST':
        project_form = PostProjectForm(request.POST, request.FILES)
        if project_form.is_valid(): 
            project_form.save()
            return redirect('Freelancing:view_project')
        else:
            messages.error(request, "Error")
    else:
        project_form = PostProjectForm()
    return render(request, 'post_project.html',{'project_form':project_form })


def view_project(request):
    all_project = ProjectDetail.objects.all()
    context = {
        'all_project':all_project
    }
    return render(request, 'project_detail.html', context)

def view_project_detail(request,id):
    project = ProjectDetail.objects.get(id=id)
    context = {
        'project':project
    }
    return render(request, 'view_project_detail.html', context)
# class PostProject(CreateView):
#     pass

def batuwa(request):
    return render(request, 'batuwas.html')

def task(request):
    return render(request, 'tasks.html')

def task_detail(request):
    return render(request, 'task_detail.html')