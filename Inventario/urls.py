"""Inventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from bodega.views import *

urlpatterns = [

    path('',index, name='index'),
    path('UsuarioList/', UsuarioList.as_view(),name="UsuarioList"),
    path('UsuarioCreate/', UsuarioCreate.as_view(),name="UsuarioCreate"),
    path('UsuarioUpdate/<pk>', UsuarioUpdate.as_view(),name="UsuarioUpdate"),
    path('RecursoCreate/', RecursoCreate.as_view(),name="RecursoCreate"),
    path('RecursoUpdate/<pk>', RecursoUpdate.as_view(),name="RecursoUpdate"),
    path('RecursoList/', RecursoList.as_view(),name="RecursoList"),
    path('AsignacionList/', AsignacionList.as_view(),name="AsignacionList"),
    path('consultarrecursos/', consultarrecursos,name="consultarrecursos"),
    path('showasignacion/', showasignacion,name="showasignacion"),
    path('AsignacionCreate/', AsignacionCreate.as_view(),name="AsignacionCreate"),
#    path('showusers/',showusers, name='showusers'),
]
