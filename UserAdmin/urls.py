from django.urls import path
app_name = 'UserAdmin'
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard_admin'),
    path('categories/',views.categories, name='categories'),
    path('users/',views.users, name='users'),
    path('providers/',views.providers, name='providers'),
    path('projects/',views.projects, name='projects'),
    path('update-project/<int:id>/',views.update_project, name='update_project',),
    path('delete-project/<int:id>/',views.delete_project, name='delete_project',),

    path('reports/',views.reports, name='reports'),
    path('fees/',views.fees, name='fees'),
    path('taxs/',views.taxs, name='taxs'),
    path('roles/',views.roles, name='roles'),
    path('roles-permission/',views.roles_permission, name='roles_permission'),
    path('skills/',views.skills, name='skills'),
    path('verify-identity/',views.verify_identity, name='verify_identity'),
    path('profiles/',views.profiles, name='profiles'),
    path('settings/',views.settings, name='settings'),
    # path('website/<int:id>/',views.website, name='website'),
    path('localization/',views.localization, name='localization'),
    path('payment-setting/',views.payment_setting, name='payment_setting'),
    path('email-setting/',views.email_setting, name='email_setting'),
    path('social-media/',views.social_media, name='social_media'),
    path('social-links/',views.social_links, name='social_links'),
    path('seo-settings/',views.seo_settings, name='seo_settings'),
    path('others/',views.others, name='others'),
    

]

