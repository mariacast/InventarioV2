from django import forms

from .models import *


class UserNewForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = [
        'identificacion',
        'nombres',
        'apellidos'
        ]

        labels={
        'identificacion' : 'Documento:',
        'nombres' : 'Nombre:',
        'apellidos' : 'Apellidos:'
        }
        widgets ={
        'identificacion':forms.TextInput(attrs={'class':'form-control','placeholder': 'Documento','type':'number'}),
        'nombres':forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombres',}),
        'apellidos':forms.TextInput(attrs={'class':'form-control','placeholder': 'Apellidos',}),
        }


class RecursoNewForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields =[
        'nombre',
        'categoria',
        'codigo',
        'marca',
        'serie',
        ]

        labels ={
        'nombre':'Recurso',
        'categoria':'Categoria',
        'codigo':'Codigo',
        'marca':'Marca',
        'serie':'Serie',
        }
        widgets={
        'nombre':forms.TextInput(attrs={'class':'form-control','placeholder': 'Nombre Recurso'}),
        'categoria':forms.TextInput(attrs={'class':'form-control','placeholder': 'Categoria',}),
        'codigo':forms.TextInput(attrs={'class':'form-control','placeholder': 'Codigo','type':'number'}),
        'marca':forms.TextInput(attrs={'class':'form-control','placeholder': 'Marca',}),
        'serie':forms.TextInput(attrs={'class':'form-control','placeholder': 'Serie',}),
        }
#'nombre':forms.Select(queryset=Usuario.objects.all()),
class AsignacionForm(forms.ModelForm):
    class Meta:
        model = RecursoUsuario

        fields =[
        'usuario',
        'recurso',
        ]

        labels ={
        'usuario':'Usuarios:',
        'recurso':'Recursos:',
        }
        widgets={
        'usuario':forms.Select(attrs={'class':'form-control','placeholder': 'Usuarios'}),
        #'usuario':ModelChoiceField(queryset=Usuario.objects.all()),
        #'recurso':ModelChoiceField(queryset=Recurso.objects.nombre()),
        'recurso':forms.Select(attrs={'class':'form-control','placeholder': 'Recursos',}),

        }

class HistorialForm(forms.ModelForm):
    class Meta:
        model = Historial
        fields =[
        'usuario',
        'recurso',
        'fecha',
        ]

        labels ={
        'usuario':'Usuarios:',
        'recurso':'Recursos:',
        }
