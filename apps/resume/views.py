from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Resume
from apps.people.models import Person


# Create your views here.
class ResumeViewSet(TemplateView):
    template_name = "resume/resume.html"

    def get(self, request, username=None, *args, **kwargs):
        user = Person.objects.filter(username=username).first()
        resume = Resume.objects.filter(created_by=user).first()

        return render(
            request, self.template_name, context={"resume": resume, "owner": user}
        )
