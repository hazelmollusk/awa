from django.contrib.auth.backends import ModelBackend
from .models import Person


class AwaBackend(ModelBackend):
    # def authenticate(self, request, username = None, password = None, **kwargs):
    #     return super().authenticate(request)

    # def has_perm(self, user_obj, perm, obj=None):
    #     return True

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Person.objects.get(username=username)
            return user if user.check_password(password) else None
        except Person.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Person.objects.get(pk=user_id)
        except Person.DoesNotExist:
            return None

    def user_can_authenticate(self, user):
        # return super().user_can_authenticate(user)
        return True
