from django.urls import path
app_name = 'UserAdmin'
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboardAdmin'),
    path('categories/',views.categories, name='categories'),
    path('users/',views.users, name='users'),
    path('providers/',views.providers, name='providers'),
    path('projects/',views.projects, name='projects'),
    path('reports/',views.reports, name='reports'),
    path('fees/',views.fees, name='fees'),
    path('taxs/',views.taxs, name='taxs'),
    path('roles/',views.roles, name='roles'),
    path('rolesPermission/',views.rolesPermission, name='rolesPermission'),
    path('skills/',views.skills, name='skills'),
    path('verifyIdentity/',views.verifyIdentity, name='verifyIdentity'),
    path('profiles/',views.profiles, name='profiles'),
    path('settings/',views.settings, name='settings'),
    path('localization/',views.localization, name='localization'),
    path('paymentSetting/',views.paymentSetting, name='paymentSetting'),
    path('emailSetting/',views.emailSetting, name='emailSetting'),
    path('socialMedia/',views.socialMedia, name='socialMedia'),
    path('socialLinks/',views.socialLinks, name='socialLinks'),
    path('seoSettings/',views.seoSettings, name='seoSettings'),
    path('others/',views.others, name='others'),
    

]

