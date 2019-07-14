from django.db import models
from datetime import datetime
class Usuario(models.Model):
    identificacion = models.CharField(max_length=15)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.nombres+" "+self.apellidos)

class Recurso(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    codigo = models.IntegerField()
    marca = models.CharField(max_length=20)
    serie = models.CharField(max_length=30)
    def __str__(self):
        return '{}'.format(self.nombre)

class RecursoUsuario(models.Model):
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    recurso = models.ForeignKey('Recurso', models.DO_NOTHING)

class Historial(models.Model):
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    recurso = models.ForeignKey('Recurso', models.DO_NOTHING)
    fecha = models.DateField(default=datetime.now())
