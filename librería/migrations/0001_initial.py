# Generated by Django 5.0.4 on 2024-04-22 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autor",
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
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Libro",
            fields=[
                (
                    "isbn",
                    models.CharField(max_length=13, primary_key=True, serialize=False),
                ),
                ("título", models.CharField(max_length=255)),
                ("editorial", models.CharField(max_length=255, null=True)),
                ("género", models.CharField(max_length=50, null=True)),
                ("lenguaje", models.CharField(max_length=50, null=True)),
                ("año_publicación", models.PositiveIntegerField(null=True)),
                ("número_páginas", models.PositiveIntegerField(null=True)),
                ("puntuación", models.PositiveIntegerField(blank=True, null=True)),
                ("color_principal", models.CharField(max_length=6)),
                ("portada", models.ImageField(null=True, upload_to="")),
                ("número_notas", models.IntegerField(default=0)),
                ("es_favorito", models.BooleanField(default=False)),
                ("autores", models.ManyToManyField(to="librería.autor")),
            ],
            options={
                "db_table": "Libros",
            },
        ),
        migrations.CreateModel(
            name="Nota",
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
                ("contenido", models.TextField()),
                ("tipo", models.CharField(max_length=50)),
                ("número_página", models.IntegerField(null=True)),
                ("referencia", models.TextField(null=True)),
                ("imagen", models.ImageField(null=True, upload_to="")),
                ("definición", models.TextField(null=True)),
                ("fecha_modificada", models.DateTimeField(auto_now=True)),
                (
                    "creada_por",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.usuario",
                    ),
                ),
                (
                    "libro_asociado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="librería.libro"
                    ),
                ),
            ],
            options={
                "db_table": "Notas",
            },
        ),
        migrations.AddIndex(
            model_name="libro",
            index=models.Index(fields=["isbn"], name="Libros_isbn_2d7eb5_idx"),
        ),
        migrations.AddIndex(
            model_name="nota",
            index=models.Index(fields=["id"], name="Notas_id_cd3a60_idx"),
        ),
    ]
