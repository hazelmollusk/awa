# Generated by Django 5.1 on 2025-02-27 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tuhi", "0003_remove_pagesection_content"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pagesection",
            old_name="content2",
            new_name="content",
        ),
    ]
