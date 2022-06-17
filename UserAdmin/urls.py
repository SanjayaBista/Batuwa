from django.urls import path
app_name = 'UserAdmin'
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboardAdmin'),
    path('categories/',views.categories, name='categories'),
]

