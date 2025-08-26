from django.db import models
from django.contrib.auth.models import AbstractUser
from django_currentuser.db.models import CurrentUserField
from guardian.mixins import GuardianUserMixin
from guardian.models import GroupObjectPermissionAbstract, UserObjectPermissionAbstract

from .managers import PersonManager


class AuditedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_by = CurrentUserField(
        related_name="%(app_label)s_%(class)s_created", on_delete=models.SET_DEFAULT
    )
    modified_by = CurrentUserField(
        on_update=True,
        related_name="%(app_label)s_%(class)s_modified",
        on_delete=models.SET_DEFAULT,
    )

    class Meta:
        abstract = True


class Person(AbstractUser, GuardianUserMixin, AuditedMixin):
    # fields go here

    REQUIRED_FIELDS = []

    objects = PersonManager()


class Profile(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=18, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        verbose_name = "profile"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
