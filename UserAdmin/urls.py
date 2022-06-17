from django.urls import path
app_name = 'UserAdmin'
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboardAdmin'),
    path('categories/',views.categories, name='categories'),
    path('users/',views.users, name='users'),
    path('providers/',views.providers, name='providers'),

]

