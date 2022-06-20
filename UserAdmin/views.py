from django.shortcuts import render
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
    context = {
        'allProj':allProj,
        'countProj':countProj
    }
    return render(request, 'projects.html',context)

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