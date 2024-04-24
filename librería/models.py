from django.db import models

from usuarios.models import Usuario

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

class Libro(models.Model):
    """
    Representa un libro leído por el usuario/a.
    """

    isbn = models.CharField(primary_key=True, max_length=13)
    título = models.CharField(max_length=255)
    autores = models.ManyToManyField(Autor)
    editorial = models.CharField(max_length=255, null=True)
    género = models.CharField(max_length=50, null=True)
    lenguaje = models.CharField(max_length=50, null=True)
    año_publicación = models.PositiveIntegerField(null=True)
    número_páginas = models.PositiveIntegerField(null=True)
    color_principal = models.CharField(max_length=6) # HEX
    portada = models.ImageField(null=True)
    número_notas = models.IntegerField(default=0)

    class Meta:
        db_table = "Libros"
        indexes = [
            models.Index(fields=["isbn"])
        ]
    
    def __str__(self) -> str:
        return self.título

class Nota(models.Model):
    """
    Representa una nota en un libro.
    """

    libro_asociado = models.ForeignKey(Libro, on_delete=models.CASCADE)
    creada_por = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    tipo = models.CharField(max_length=50)
    número_página = models.IntegerField(null=True)
    referencia = models.TextField(null=True)
    imagen = models.ImageField(null=True)
    definición = models.TextField(null=True)
    fecha_modificada = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Notas"
        indexes = [
            models.Index(fields=["id"])
        ]

    def __str__(self) -> str:
        return self.contenido[0:20] + "..."
    
class ListaDeLectura(models.Model):
    """
    Representa la relación entre un libro y un usuario.
    """

    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    fecha_añadido = models.DateField(auto_now_add=True)
    fecha_empezado = models.DateField(null= True)
    fecha_terminado = models.DateField(null=True)
    puntuación = models.PositiveIntegerField(null=True, blank=True)
    es_libro_favorito = models.BooleanField(default=False)

    class Meta:
        db_table = "ListaDeLectura"
