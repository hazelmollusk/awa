# Generated by Django 5.1 on 2025-03-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tuhi", "0005_pagesection_draft_alter_pagesection_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="visible",
            field=models.BooleanField(default=False),
        ),
    ]
