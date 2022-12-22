from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TasksForm, AlumnosForm, ProfesoresForm
from .models import Tarea, Alumnos
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def niveles_alumnos(request):
    return render(request, 'niveles_alumnos.html')

def cuentaProfesores(request):
    return render(request, 'cuenta_profesores.html')

def cuenta(request):
    return render(request, 'cuenta.html')

@login_required
def tasks(request):
    tasks = Tarea.objects.filter(user=request.user, dateCompleted__isnull=True)
    return render(request, 'tasks.html', {'tasks': tasks})

@login_required
def tasks_complete(request):
    tasks = Tarea.objects.filter(user=request.user, dateCompleted__isnull=False).order_by('-dateCompleted')
    return render(request, 'tasks.html', {'tasks': tasks})

@login_required
def taskDetail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Tarea, pk = task_id, user=request.user)
        form=TasksForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form':form})
    else: 
        try:
            task = get_object_or_404(Tarea, pk = task_id, user=request.user)
            form = TasksForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form':form, 'error': 'Error al actulizar su tarea'})
            
@login_required            
def complete_task(request, task_id):
    task = get_object_or_404(Tarea, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.dateCompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Tarea, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    
@login_required
def createTasks(request):
    if request.method == 'GET':
        return render(request, 'create_tasks.html', {'form': TasksForm})
    else:
        try:
            form = TasksForm(request.POST)
            new_task = form.save(commit = False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_tasks.html', {'form': TasksForm, 'error':'Coloque un dato valido' })
            
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('cuenta')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, 'error': "Este usuario ya existe"})
        return render(request, 'signup.html', {'form': UserCreationForm, 'error': "Las contraseñas no coinciden"})
    
def signout(request):
    logout(request)
    return redirect('login')

def agregar_alumnos(request):
    if request.method == 'GET':
        form=AlumnosForm()
        return render(request, 'signin_alumnos.html', {'form':form})
    else: 
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin_alumnos.html', {'form': AuthenticationForm, "error": 'Su nombre o contraseña es incorrecta'})
        else:
            login(request, user)
            return redirect('niveles')
        
def agregar_profesor(request):
    if request.method == 'GET':
        form=ProfesoresForm()
        return render(request, 'signin_profesores.html', {'form':form})
    else: 
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin_profesores.html', {'form': AuthenticationForm, "error": 'Su nombre o contraseña es incorrecta'})
        else:
            login(request, user)
            return redirect('niveles')










