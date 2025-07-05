from django.contrib import admin
from django import forms

from guardian.admin import GuardedModelAdmin, GuardedModelAdminMixin
from nested_admin import NestedModelAdmin, NestedStackedInline

# from mce_filebrowser.admin import MCEFilebrowserAdmin
# from markdownx.admin import MarkdownxModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.fields import SummernoteTextField

from .models import Post, Comment

AUDIT_FIELDS = ["created_by", "created", "modified"]


class PostAdmin(SummernoteModelAdmin): pass

admin.site.register(Post, PostAdmin)
