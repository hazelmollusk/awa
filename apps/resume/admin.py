from django.contrib import admin
from .models import Resume, Job, Organization, Education, Certification, Skill

# Register your models here.
admin.site.register(Resume, Job, Organization, Education, Certification, Skill)
