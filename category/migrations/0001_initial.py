# Generated by Django 4.2.4 on 2023-08-02 07:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category_name", models.CharField(max_length=255, unique=True)),
                ("slug", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField(blank=True, max_length=500)),
                (
                    "cat_image",
                    models.ImageField(blank=True, upload_to="photos/categories/"),
                ),
            ],
        ),
    ]
