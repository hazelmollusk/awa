# Generated by Django 5.1 on 2023-12-03 19:51

import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware
from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mbme", "0004_sociallink"),
    ]

    operations = [
        migrations.AddField(
            model_name="sociallink",
            name="creator",
            field=django_currentuser.db.models.fields.CurrentUserField(
                default=django_currentuser.middleware.get_current_authenticated_user,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
