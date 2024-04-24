from django.core.validators import MinLengthValidator
from django.db import models

class Usuario(models.Model):
    """
    Representa a una persona que utiliza la aplicación.
    """

    nombre = models.CharField(max_length=150, validators=[MinLengthValidator])

    class Meta:
        db_table = "Usuarios"


