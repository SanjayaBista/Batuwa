from django.urls import path, include
app_name = 'Freelancing'
from Freelancing.views import home, userLogin, userRegister
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.userLogin, name="login"),
    path('register/', views.userRegister, name="register"),
    path('postProject/', views.postProject, name="postProject"),
    path('viewProject/', views.viewProject, name="viewProject"),
    path('viewProjectDetail/<int:id>/', views.viewProjectDetail, name="viewProjectDetail"),
  
]