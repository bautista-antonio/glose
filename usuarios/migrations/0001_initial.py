# Generated by Django 5.0.4 on 2024-04-22 13:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuario",
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
                (
                    "nombre",
                    models.CharField(
                        max_length=150,
                        validators=[django.core.validators.MinLengthValidator],
                    ),
                ),
            ],
        ),
    ]
