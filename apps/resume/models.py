from django.db import models
from awa.apps.people.models import AuditedMixin


# Create your models here.
class Resume(AuditedMixin, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
