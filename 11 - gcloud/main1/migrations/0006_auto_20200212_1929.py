# Generated by Django 3.0.2 on 2020-02-12 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main1", "0005_auto_20200212_1908"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tutorial", name="tutorial_series",
        ),
        migrations.RemoveField(
            model_name="tutorial", name="tutorial_slug",
        ),
    ]
