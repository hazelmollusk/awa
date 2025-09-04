from django.urls import path
from .views import ResumeViewSet

urlpatterns = [
    path("", ResumeViewSet.as_view(), name="resume"),
]
