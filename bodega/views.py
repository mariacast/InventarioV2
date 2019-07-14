from datetime import datetime, date, time, timedelta
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.shortcuts import render , render_to_response, redirect
from django.template import RequestContext
from django.urls import reverse_lazy
from .forms import *

def index(request):

    return render(request,'index.html')

class UsuarioList(ListView):
    model = Usuario
    template_name= 'showusers.html'

class RecursoList(ListView):
    model = Recurso
    template_name= 'showrecursos.html'
class AsignacionList(ListView):
    model = RecursoUsuario
    template_name= 'showasignacion.html'

def showasignacion(request):
    asignaciones = RecursoUsuario.objects.all()
    recursos = Recurso.objects.all()
    users = Usuario.objects.all()
    return render(request,'showasignacion.html',{'recursos':recursos,'users':users})

def consultarrecursos(request):

    if request.method == 'POST':
        user = request.POST['id_user']
        U= Usuario.objects.get(id=user)
        list =[]
        Urecursos = RecursoUsuario.objects.filter(usuario_id=user)
        for r in Urecursos:
            recurso = Recurso.objects.get(id=r.recurso_id)
            list.append({'nombre':recurso.nombre,'categoria':recurso.categoria,'marca':recurso.marca})
        print(list)
        return render(request,'showconsultas.html',{'list':list,'U':U})


class UsuarioCreate(CreateView):
    model: Usuario
    form_class = UserNewForm
    template_name= 'userRegistro.html'
    success_url = reverse_lazy('UsuarioList')

class UsuarioUpdate(UpdateView):
    model: Usuario
    form_class = UserNewForm
    queryset =Usuario.objects.all()
    template_name= 'userRegistro.html'
    success_url = reverse_lazy('UsuarioList')

class RecursoCreate(CreateView):
    model: Recurso
    form_class = RecursoNewForm
    template_name= 'recursosregistro.html'
    success_url = reverse_lazy('RecursoList')

class RecursoUpdate(UpdateView):
    model: Recurso
    form_class = RecursoNewForm
    queryset =Recurso.objects.all()
    template_name= 'recursosregistro.html'
    success_url = reverse_lazy('RecursoList')

class AsignacionCreate(CreateView):
    model = RecursoUsuario
    form_class = AsignacionForm
    template_name ='asignar.html'
    success_url = reverse_lazy('RecursoCreate')
