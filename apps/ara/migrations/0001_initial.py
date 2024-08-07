# Generated by Django 5.0.6 on 2024-07-19 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.CreateModel(
            name="Context",
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
            ],
        ),
        migrations.CreateModel(
            name="ContextPath",
            fields=[
                (
                    "context_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="ara.context",
                    ),
                ),
                ("path", models.SlugField()),
                (
                    "parent",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="ara.context",
                    ),
                ),
            ],
            bases=("ara.context",),
        ),
        migrations.CreateModel(
            name="ContextRoot",
            fields=[
                (
                    "context_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="ara.context",
                    ),
                ),
                ("project_name", models.CharField(max_length=32, unique=True)),
                ("default_path", models.CharField(default="index", max_length=128)),
            ],
            bases=("ara.context",),
        ),
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
        migrations.CreateModel(
            name="SiteContext",
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
                (
                    "site",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="sites.site"
                    ),
                ),
                (
                    "context_root",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ara.contextroot",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="contextroot",
            name="sites",
            field=models.ManyToManyField(through="ara.SiteContext", to="sites.site"),
        ),
        migrations.CreateModel(
            name="ContentNode",
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
                ("object_id", models.PositiveIntegerField(null=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            bases=("ara.contextpath",),
        ),
        migrations.AddIndex(
            model_name="contextpath",
            index=models.Index(
                fields=["parent", "path"], name="ara_context_parent__c56010_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="contextpath",
            constraint=models.UniqueConstraint(
                condition=models.Q(
                    ("parent__isnull", True), ("path__isnull", True), _negated=True
                ),
                fields=("path", "parent"),
                name="ara_contextpath_unique_context_path",
                nulls_distinct=True,
            ),
        ),
        migrations.AddIndex(
            model_name="contentnode",
            index=models.Index(
                fields=["content_type", "object_id"],
                name="ara_content_content_0516a9_idx",
            ),
        ),
    ]
