from django.urls import path, include
app_name = 'Freelancing'
from .import views
urlpatterns = [
    path('', views.home, name="home")
  
]