# Generated by Django 4.1 on 2024-05-20 06:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="description",
        ),
    ]
