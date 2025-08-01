# Generated by Django 5.2.3 on 2025-07-29 18:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("libros", "0002_alter_libro_imagen"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Opinion",
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
                ("texto", models.TextField(verbose_name="Opinion")),
                ("fecha", models.DateTimeField(auto_now_add=True)),
                (
                    "libro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="libros.libro"
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-fecha"],
            },
        ),
    ]
