from django.urls import path

from . import views

urlpatterns= [
    path("", views.librería, name="librería"),
    path("<int:usuario_id>", views.libro_nuevo, name="libro_nuevo"),
    path("<int:libro_id>", views.vista_libro, name="vista_libro"),
]