
from django.urls import path, include

from .views import view_page

urlpatterns = [
    path("<slug:slug>/", view_page),
]
