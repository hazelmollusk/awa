from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Person


class PersonCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Person


class PersonChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = Person

