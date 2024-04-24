# Generated by Django 5.0.4 on 2024-04-22 21:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("librería", "0001_initial"),
        ("usuarios", "0002_alter_usuario_table"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="libro",
            name="es_favorito",
        ),
        migrations.RemoveField(
            model_name="libro",
            name="puntuación",
        ),
        migrations.CreateModel(
            name="ListaDeLectura",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("estado", models.CharField(max_length=50)),
                ("fecha_añadido", models.DateField(auto_now_add=True)),
                ("fecha_empezado", models.DateField(null=True)),
                ("fecha_terminado", models.DateField(null=True)),
                ("puntuación", models.PositiveIntegerField(blank=True, null=True)),
                ("es_libro_favorito", models.BooleanField(default=False)),
                (
                    "libro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="librería.libro"
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.usuario",
                    ),
                ),
            ],
            options={
                "db_table": "ListaDeLectura",
            },
        ),
    ]
