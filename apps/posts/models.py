from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.fields import TextField, UUIDField

from django_summernote.fields import SummernoteTextField

from apps.people.models import AuditedMixin

content_page_field = lambda: SummernoteTextField()
content_post_field = lambda: SummernoteTextField()
content_comment_field = lambda: TextField()


class Post(AuditedMixin):
    uuid = UUIDField()
    content = content_post_field()
    def str(self):
        return slugify(self.content)[0:20]
    
    @property
    def context_path(self):
        return str(self)

class Comment(AuditedMixin):
    content = content_comment_field()
    def str(self):
        return slugify(self.content)[0:20]
    
    @property
    def context_path(self):
        return str(self)


