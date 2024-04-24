from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader

from .models import Libro

def librería(request: HttpRequest):
    usuario = request.user.id
    libros_usuario = Libro.objects.filter()
    plantilla = loader.get_template("librería/index.py")
    contexto = {
        "libros_usuario": libros_usuario
    }
    return HttpResponse(f"Esta es la librería del usuario: {usuario}.")

def libro_nuevo(request, usuario_id):
    return HttpResponse(f"Usuario con ID {usuario_id} está añadiendo un libro.")

def vista_libro(request, libro_id):
    return HttpResponse(f"Este libro ({libro_id}) pertenece a un usuario.")