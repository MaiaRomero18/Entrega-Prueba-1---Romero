from django.forms import ModelForm
from .models import Tarea, Alumnos, Profesor

class TasksForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['title', 'descripcion']
     
class AlumnosForm(ModelForm):
    class Meta:
        model = Alumnos
        fields = ['nombre', 'apellido', 'nivel', 'mail']
        
class ProfesoresForm(ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido']
        