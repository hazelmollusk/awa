from django.contrib import admin
from .models import Resume, Job, Organization, Education, Certification, Skill

# Register your models here.
admin.site.register(Resume)
admin.site.register(Job)
admin.site.register(Organization)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Skill)
