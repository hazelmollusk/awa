from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from tinymce.models import HTMLField
from ckedi

from apps.mana.models import AuditedMixin
from apps.rakau.models import Context, ContentMixin



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
    content = HTMLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "section"


class Post(AuditedMixin, ContentMixin):
    content = HTMLField()
    def str(self):
        return slugify(self.content)[0:20]
    
    @property
    def context_path(self):
        return str(self)

class Comment(AuditedMixin, ContentMixin):
    content = HTMLField()
    def str(self):
        return slugify(self.content)[0:20]
    
    @property
    def context_path(self):
        return str(self)


