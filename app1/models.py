from django.db import models
from django.contrib.auth.models import User


class Tarea(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    dateCompleted = models.DateTimeField(null=True)
    user = models.name = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + '- by ' + self.user.username

    
class Alumnos(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    mail= models.CharField(max_length=280)
    nivel= models.CharField(max_length=100)
    
class Profesor(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)

    
    
    
    