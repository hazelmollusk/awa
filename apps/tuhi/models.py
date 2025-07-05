from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.fields import TextField

# from tinymce.models import HTMLField
# from ckeditor.fields import RichTextField
# from markdownx.models import MarkdownxField
from django_summernote.fields import SummernoteTextField

from apps.mana.models import AuditedMixin
from apps.rakau.models import Context, ContentMixin

content_page_field = lambda: SummernoteTextField()
content_post_field = lambda: SummernoteTextField()
content_comment_field = lambda: TextField()

class PostContainer(models.Model):
    class Meta:
        abstract = True


class Folder(AuditedMixin, ContentMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=False)  # FIXME
    # slug should be unique_together with parent context

    def __str__(self):
        return self.title[0:20]

    def save(self, *a, **kw):
        if not self.slug:
            self.slug = Context.objects.slugify(self.title)
        super().save(*a, **kw)

    @property
    def context_path(self):
        return self.slug


class Page(Folder):
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
    section = models.ForeignKey(PageSection, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField()
    title = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        verbose_name = 'image'

class Post(AuditedMixin, ContentMixin):
    content = content_post_field()
    def str(self):
        return slugify(self.content)[0:20]
    
    @property
    def context_path(self):
        return str(self)

class Comment(AuditedMixin, ContentMixin):
    content = content_comment_field()
    def str(self):
        return slugify(self.content)[0:20]
    
    @property
    def context_path(self):
        return str(self)


