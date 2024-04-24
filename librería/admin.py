from django.contrib import admin

from .models import Libro
from .models import Nota
from .models import ListaDeLectura

admin.site.register(Libro)
admin.site.register(Nota)
admin.site.register(ListaDeLectura)
