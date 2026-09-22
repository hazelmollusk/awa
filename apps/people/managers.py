from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group
from django_currentuser.db.models import CurrentUserField
from guardian.models import (
    UserObjectPermissionAbstract,
    GroupObjectPermissionAbstract,
)
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class PersonManager(BaseUserManager):
    def create_user(self, **kw):
        # auth could come from anywhere, so we may not
        # have things like email, or even a password
        user = self.model(**kw)
        if 'password' in kw:
            user.set_password(kw['password'])
        user.save()
        return user

    def create_superuser(self, **kw):
        user = self.create_user(**kw)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
