from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Resume
from apps.people.models import Person
import logging

log = logging.getLogger(__name__)


# Create your views here.
class ResumeViewSet(TemplateView):
    template_name = "resume/resume.html"

    def get(self, request, username=None, *args, **kwargs):
        owner = Person.objects.filter(username=username).first()
        resume = Resume.objects.filter(created_by=owner).first()
        log.warning(f"username for resume: {username}")
        log.warning(f"owner for resume: {owner}")
        log.warning(f"resume for resume: {resume}")

        return render(
            request, self.template_name, context={"resume": resume, "owner": owner}
        )
