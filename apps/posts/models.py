import uuid

from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.fields import TextField, UUIDField

from django_summernote.fields import SummernoteTextField

from apps.people.models import AuditedMixin

content_post_field = lambda: SummernoteTextField()
content_comment_field = lambda: TextField()


class UUIDModel(models.Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Post(UUIDModel, AuditedMixin):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = content_post_field()

    def __str__(self):
        return f"Post by {self.created_by}"

    class Meta:
        indexes = [models.Index(fields=["content"])]

        ordering = ["-modified"]

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.uuid)])


class Comment(UUIDModel, AuditedMixin):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    content = content_comment_field()

    def str(self):
        return slugify(self.content)[0:20]

    class Meta:
        indexes = [models.Index(fields=["post"]), models.Index(fields=["parent"])]
