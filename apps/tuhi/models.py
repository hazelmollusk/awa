from django.db import models
from django.shortcuts import reverse
from django_quill.fields import QuillField
from django_currentuser.db.models import CurrentUserField

from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
import re

from apps.mana.models import AuditedMixin
from apps.ara.models import ContextMixin, ContextRoot



class Page(AuditedMixin, ContextMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = QuillField()

    def __str__(self):
        return self.title

    def get_parent_context(self):
        return ContextRoot.objects.first()

    def get_context_path(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("page", kwargs={"pk": self.pk})


class Folder(AuditedMixin, ContextMixin):
    title = models.CharField(max_length=255)
