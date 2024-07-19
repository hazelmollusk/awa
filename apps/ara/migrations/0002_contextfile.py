# Generated by Django 5.0.6 on 2024-07-18 16:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ara", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContextFile",
            fields=[
                (
                    "contextpath_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="ara.contextpath",
                    ),
                ),
                ("file", models.FileField(upload_to="")),
            ],
            bases=("ara.contextpath",),
        ),
    ]
