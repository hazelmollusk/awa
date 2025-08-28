from django.db import models
from django.urls import reverse
from apps.people.models import AuditedMixin
from apps.pages.models import content_page_field


# Create your models here.
class Resume(AuditedMixin, models.Model):
    owner = models.OneToOneField("people.Person", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = content_page_field()
    skills = models.ManyToManyField("Skill", blank=True)
    education = models.ManyToManyField("Education", blank=True)
    certifications = models.ManyToManyField("Certification", blank=True)

    def get_absolute_url(self):
        return reverse("resume_detail", kwargs={"username": self.owner.username})

    def __str__(self):
        return f"{self.owner.first_name}'s Resume: {self.title}"


class Organization(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(blank=True, null=True, upload_to="resume/companies/")
    is_school = models.BooleanField(default=False)

    # description = content_page_field()
    def __str__(self):
        return self.name


class Job(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Organization, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = content_page_field(blank=True, null=True)

    def __str__(self):
        return f"{self.resume.owner.full_name}: {self.title} at {self.company.name}"

    class Meta:
        ordering = ["-end_date"]


class Education(models.Model):
    school = models.ForeignKey(Organization, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100, blank=True, null=True)
    field_of_study = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    # description = content_page_field()


class Certification(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, blank=True, null=True
    )
    date = models.DateField()
    # description = content_page_field()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-date"]


class Skill(models.Model):
    name = models.CharField(max_length=100)
    # description = content_page_field()

    def __str__(self):
        return self.name
