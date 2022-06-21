from tracemalloc import start
from turtle import title
from webbrowser import get
from django.shortcuts import redirect, render
from Freelancing.models import ProjectDetail
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
    allProj = ProjectDetail.objects.all()
    countProj = ProjectDetail.objects.count()
    active_count = ProjectDetail.objects.filter(project_status = True).count()
    inactive_count = ProjectDetail.objects.filter(project_status = False).count()
    active_project = ProjectDetail.objects.filter(project_status = True)
    inactive_project = ProjectDetail.objects.filter(project_status = False)
    context = {
        'allProj':allProj,
        'countProj':countProj,
        'countActive':active_count,
        'countInactive':inactive_count,
        'activeProj':active_project,
        'InactiveProj':inactive_project

    }
    return render(request, 'projects.html',context)

def update_project(request, id):
    getProj = ProjectDetail.objects.all()
    context = {
        'getProj':getProj
    }
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        technology = request.POST.get('technology')
        company = request.POST.get('company')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        project = ProjectDetail.objects.get(id=id)
        project.title = title
        project.price = price
        project.technology = technology
        project.company = company
        project.start_date = start_date
        project.end_date = end_date
        project.save()
        return redirect('UserAdmin:projects')
    return render (request, 'projects.html',context)

def delete_project(request,id):
    delProj = ProjectDetail.objects.filter(id=id)
    delProj.delete()
    context = {
        'delProj':delProj
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

def rolesPermission(request):
    return render(request, 'rolesPermissions.html')

def skills(request):
    return render(request, 'skills.html')

def verifyIdentity(request):
    return render(request, 'verifyIdentity.html')

def profiles(request):
    return render(request, 'profiles.html')

def settings(request):
    return render(request, 'settings.html')

def localization(request):
    return render(request, 'localization.html')

def paymentSetting(request):
    return render(request, 'paymentSetting.html')

def emailSetting(request):
    return render(request, 'emailSetting.html')

def socialMedia(request):
    return render(request, 'socialMedia.html')

def socialLinks(request):
    return render(request, 'socialLinks.html')

def seoSettings(request):
    return render(request, 'seoSettings.html')

def others(request):
    return render(request, 'others.html')