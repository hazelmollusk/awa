# Generated by Django 5.2.dev20240719125256 on 2024-07-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tuhi", "0004_pagedraft"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pagesection",
            name="title",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]
