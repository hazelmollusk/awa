from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import AwaUser


class AwaUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = AwaUser


class AwaUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = AwaUser
