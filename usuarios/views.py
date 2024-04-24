from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader

from .forms import FormularioInicioSesión
from .forms import FormularioRegistroUsuario
from .models import Usuario


def registrar_usuario(petición: HttpRequest):
    """
    Vista para manejar el registro de usuarios.
    """
    if petición.method == "POST":
        formulario = FormularioRegistroUsuario(petición.POST)
        if formulario.es_válido():
            usuario = formulario.save()
            iniciar_sesión(petición, usuario)
            return redirect("librería")
        
    else:



def iniciar_sesión(petición: HttpRequest):
    """
    !!!
    """


def cerrar_sesión(petición: HttpRequest):
    """
    !!!
    """
