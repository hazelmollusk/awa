from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ResumeViewSet(TemplateView):
    template_name = "resume/resume.html"

    def get(self, request):
        return render(request, self.template_name)
