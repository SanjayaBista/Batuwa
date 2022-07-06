from tkinter import SE
from django.utils import timezone
from os import system
from tracemalloc import start
from turtle import title
from webbrowser import get
from django.shortcuts import get_object_or_404, redirect, render
from requests import request

from Batuwa.settings import TIME_ZONE
from Freelancing.models import ProjectDetail
from .forms import AddressForm, LocalizationForm, WebsiteForm, ProjectForm
from Freelancing.models import ProjectDetail
from UserAdmin.models import Country, Website, State, Address, Localization, PaypalPayment, StripePayment, SeoSetting
import pytz
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
    country_name = Country.objects.all()
    state_name = State.objects.all()
   
    if request.method == 'POST':
        setting_type = request.POST.get('type')
        if setting_type == 'website':
            website_name = request.POST.get('website_name')
            logo = request.POST.get('logo')
            favicon = request.POST.get('favicon')
            if request.user.customer.website:
                website = Website.objects.get(user=request.user.customer)
                website.website_name = website_name
                website.logo = logo
                website.favicon = favicon
            else:
                website = Website(website_name=website_name, logo=logo, favicon=favicon,user=request.user.customer)
            website.save()
            
        elif setting_type == 'address':
            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            city = request.POST.get('city')
            zip_code = request.POST.get('zip_code')
            country = request.POST.get('country')
            print('country',country)
            country_obj = Country.objects.get(name=country)
            state = request.POST.get('state')
            print('state',state)
            state_obj = State.objects.get(name=state, country_id=country_obj)
            if request.user.customer.address:
                address = Address.objects.get(user=request.user.customer)
                address.address1 = address1
                address.address2 = address2
                address.city = city
                address.zip_code = zip_code
                address.country = country_obj
                address.state = state_obj
            else:
                address = Address(address1=address1, address2=address2, city=city,zip_code=zip_code, country=country_obj,state=state_obj, user=request.user.customer)
            address.save()  
    context = {
        'country_name':country_name,
        'state_name':state_name
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
    if request.method == 'POST':
        localization_form = LocalizationForm(request.POST)
        if localization_form.is_valid():
            localization_form.save()
            return redirect('UserAdmin:localization')
      
    else:
        localization_form = LocalizationForm()
    return render(request, 'localization.html',{'localization_form':localization_form })


def payment_setting(request):
    if request.method == 'POST':
        payment_type = request.POST.get('type')
        if payment_type == 'paypal':
            option = request.POST.get('budget')
            braintree_token_key = request.POST.get('braintree_token_key')
            braintree_merchant_id = request.POST.get('braintree_merchant_id')
            braintree_public_key = request.POST.get('braintree_public_key')
            braintree_private_key = request.POST.get('braintree_private_key')
            paypal_app_id = request.POST.get('paypal_app_id')
            paypal_secret_key = request.POST.get('paypal_secret_key')
            if request.user.customer.paypalpayment:
                payment = PaypalPayment.objects.get(user=request.user.customer)
                payment.option = option
                payment.braintree_token_key = braintree_token_key
                payment.braintree_merchant_id = braintree_merchant_id
                payment.braintree_public_key = braintree_public_key
                payment.braintree_private_key = braintree_private_key
                payment.paypal_app_id = paypal_app_id 
                payment.paypal_secret_key = paypal_secret_key
                 
            else:
                payment = PaypalPayment(
                    option=option,
                    braintree_token_key=braintree_token_key,
                    braintree_merchant_id=braintree_merchant_id,
                    braintree_public_key=braintree_public_key,
                    braintree_private_key=braintree_private_key,
                    paypal_app_id=paypal_app_id,
                    paypal_secret_key=paypal_secret_key,
                    user=request.user.customer
                    )
            payment.save()
        elif payment_type == 'stripe':
            option = request.POST.get('budget')
            gateway_name = request.POST.get('gateway_name')
            api_key = request.POST.get('api_key')
            rest_key = request.POST.get('rest_key')
           
            if request.user.customer.stripepayment:
                payment = StripePayment.objects.get(user=request.user.customer)
                payment.option = option
                payment.gateway_name = gateway_name
                payment.api_key = api_key
                payment.rest_key = rest_key
                
                 
            else:
                payment = StripePayment(
                    option=option,
                    gateway_name=gateway_name,
                    api_key=api_key,
                    rest_key=rest_key,
                    user=request.user.customer
                    )
            payment.save()
                
    return render(request, 'payment_setting.html')

def email_setting(request):
    return render(request, 'email_setting.html')

def social_media(request):
    return render(request, 'social_media.html')

def social_links(request):
    return render(request, 'social_links.html')

def seo_settings(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        keyword = request.POST.get('keyword')
        description = request.POST.get('description')
        if request.user.customer.seosetting:
            data = SeoSetting.objects.get(user=request.user.customer)
            data.title = title
            data.keyword = keyword
            data.description = description    
        else:
            data = SeoSetting(
                title=title,
                keyword=keyword,
                description=description,
                user=request.user.customer
                )
        data.save()
    return render(request, 'seo_settings.html')

def others(request):
    return render(request, 'others.html')