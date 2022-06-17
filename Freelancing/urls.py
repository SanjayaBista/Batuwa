from django.urls import path, include
app_name = 'Freelancing'
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.userLogin, name="login"),
    path('register/', views.userRegister, name="register"),
  
]