from tracemalloc import start
from turtle import title
from webbrowser import get
from django.shortcuts import get_object_or_404, redirect, render
from requests import request
from Freelancing.models import ProjectDetail
from .forms import AddressForm, WebsiteForm, ProjectForm
from .models import *
# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def categories(request):
    return render(request, 'categories.html')

def users(request):
    return render(request, 'users.html')

def providers(request):
    return render(request, 'providers.html')

def projects(request):
    all_proj = ProjectDetail.objects.all()
    count_proj = ProjectDetail.objects.count()
    active_count = ProjectDetail.objects.filter(project_status='Active').count()
    inactive_count = ProjectDetail.objects.filter(project_status = 'Inactive').count()
    trash_count = ProjectDetail.objects.filter(project_status = 'Trash').count()
    active_project = ProjectDetail.objects.filter(project_status = 'Active')
    inactive_project = ProjectDetail.objects.filter(project_status = 'Inactive')
    trash_project = ProjectDetail.objects.filter(project_status = 'Trash')
    context = {
        'all_proj':all_proj,
        'count_proj':count_proj,
        'count_active':active_count,
        'count_inactive':inactive_count,
        'count_trash':trash_count,
        'active_proj':active_project,
        'inactive_proj':inactive_project,
        'trash_proj':trash_project,


    }
    return render(request, 'projects.html',context)

def update_project(request,id):

    get_proj = ProjectDetail.objects.all()
    context = {
        'get_proj':get_proj
    }
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        technology = request.POST.get('technology')
        company = request.POST.get('company')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        project_status = request.POST.get('project_status')
        project = ProjectDetail.objects.get(id=id)
        project.title = title
        project.price = price
        project.technology = technology
        project.company = company
        project.start_date = start_date
        project.end_date = end_date
        project.project_status = project_status
        project.save()
        print(project)
        return redirect('UserAdmin:projects')
    # project = get_object_or_404(ProjectDetail, pk=pk)
    # form = ProjectForm(instance=project)
    # if request.method == 'POST':
    #     form = ProjectForm(request.POST, instance=project)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('UserAdmin:projects')
    # context = {
    #     'Form':form,
    #     'allProj':allProj
    # }
    return render (request, 'projects.html',context)

def delete_project(request,id):
    del_proj = ProjectDetail.objects.filter(id=id)
    del_proj.delete()
    context = {
        'del_proj':del_proj
    }
    return redirect('UserAdmin:projects')


def reports(request):
    return render(request, 'reports.html')

def fees(request):
    return render(request, 'fees.html')

def taxs(request):
    return render(request, 'taxs.html')

def roles(request):
    return render(request, 'roles.html')

def roles_permission(request):
    return render(request, 'roles_permissions.html')

def skills(request):
    return render(request, 'skills.html')

def verify_identity(request):
    return render(request, 'verify_identity.html')

def profiles(request):
    return render(request, 'profiles.html')

def settings(request):
    form = WebsiteForm()
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('UserAdmin:settings')
    context = {
        'form':form
    }
    return render(request, 'settings.html',context)

# def website(request, pk):
#     website = get_object_or_404(Website, pk=pk)
#     form = WebsiteForm(instance=website)
#     if request.method == 'POST':
#         form = WebsiteForm(request.POST, instance=website)
#         if form.is_valid():
#             form.save()
#             return redirect('UserAdmin:settings')
#     context = {
#         'form':form
#     }
#     return render(request, 'settings.html',context)

def localization(request):
    return render(request, 'localization.html')

def payment_setting(request):
    return render(request, 'payment_setting.html')

def email_setting(request):
    return render(request, 'email_setting.html')

def social_media(request):
    return render(request, 'social_media.html')

def social_links(request):
    return render(request, 'social_links.html')

def seo_settings(request):
    return render(request, 'seo_settings.html')

def others(request):
    return render(request, 'others.html')