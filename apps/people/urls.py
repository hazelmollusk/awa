
from django.urls import path, include

from .views import view_user

urlpatterns = [
    path("~<str:username>/", view_page),
]
