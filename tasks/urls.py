"""tasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('cuenta/', views.cuenta, name="cuenta"),
    path('signup/', views.signup, name="signup"),
    path('tasks/', views.tasks, name="tasks"),
    path('tasks_completed/', views.tasks_complete, name="tasks_complete"),
    path('create/', views.createTasks, name="create"),
    path('tasks/<int:task_id>/', views.taskDetail, name="taskdetail"),
    path('tasks/<int:task_id>/complete', views.complete_task, name="complete"),
    path('tasks/<int:task_id>/delete', views.delete_task, name="delete"),
    path('logout/', views.signout, name="logout"),
    path('cuenta/signin_alumnos/', views.agregar_alumnos, name='signin_alumnos'),
    path('niveles_alumnos/', views.niveles_alumnos, name="niveles_alumnos"),
    path('cuenta/signin_profesores/', views.agregar_profesor, name='signin_profesores'),
     path('cuenta_profesores/', views.cuentaProfesores, name="cuenta_profesores")
]