# Generated by Django 3.0.2 on 2020-02-12 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_auto_20200212_1904"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tutorial", name="tutorial_series",
        ),
        migrations.RemoveField(
            model_name="tutorial", name="tutorial_slug",
        ),
    ]
