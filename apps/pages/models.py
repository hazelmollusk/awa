from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.fields import TextField

# from tinymce.models import HTMLField
# from ckeditor.fields import RichTextField
# from markdownx.models import MarkdownxField
from django_summernote.fields import SummernoteTextField

from apps.people.models import AuditedMixin

content_page_field = lambda: SummernoteTextField()


class Page(AuditedMixin):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    draft = models.BooleanField(default=True)
    visible = models.BooleanField(default=False)


class PageSection(AuditedMixin):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=255, blank=True, default="")
    draft = models.BooleanField(default=True)
    content = content_page_field()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "section"


class PageSectionImage(models.Model):
    section = models.ForeignKey(
        PageSection, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField()
    title = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "image"
