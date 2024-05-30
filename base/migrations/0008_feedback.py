# Generated by Django 5.0.6 on 2024-05-30 03:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0007_delete_book"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
            ],
        ),
    ]
