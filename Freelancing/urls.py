from django.urls import path, include
app_name = 'Freelancing'
from Freelancing.views import home, user_login, user_register, view_project, view_project_detail
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('post-project/', views.post_project, name="post_project"),
    path('view-project/', views.view_project, name="view_project"),
    path('view-project-detail/<int:id>/', views.view_project_detail, name="view_project_detail"),
    path('batuwa/', views.batuwa, name="batuwa"),
    path('task/', views.task, name="task"),
    path('task-detail/', views.task_detail, name="task_detail"),
  
]