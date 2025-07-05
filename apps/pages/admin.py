from django.contrib import admin
from django import forms

from guardian.admin import GuardedModelAdmin, GuardedModelAdminMixin
from nested_admin import NestedModelAdmin, NestedStackedInline

# from mce_filebrowser.admin import MCEFilebrowserAdmin
# from markdownx.admin import MarkdownxModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.fields import SummernoteTextField

from .models import Page, Folder, PageSection, PageSectionImage, Post, Comment

AUDIT_FIELDS = ["created_by", "created", "modified"]


class PageSectionImageAdmin(NestedStackedInline):
    model = PageSectionImage
    # fieldsets = [
    #     (None, ('title', 'image')),
    # ]
    fields = ('title','image')
    extra = 0
    min_num = 0

class PageSectionAdminForm(forms.ModelForm):
    model = PageSection
    fields = '__all__'
    widgets = {
        'content': SummernoteTextField()
    }

class PageSectionAdmin(NestedStackedInline):
    model = PageSection
    min_num = 0
    max_num = 20
    extra = 1
    fields = ("title","draft","content")
    # fieldsets = [
    #     (None, ("title", "draft")), 
    #     (None, ("content",))
    # ]
    inlines = [PageSectionImageAdmin]


@admin.register(Page)
class PageAdmin(NestedModelAdmin, GuardedModelAdminMixin):
    readonly_fields = AUDIT_FIELDS
    prepopulated_fields = {"slug": ["title"]}
    fieldsets = [
        (None, {"fields": ["title", "slug", "draft", "visible"]}),
        ("Audit", {"fields": AUDIT_FIELDS}),
    ]
    inlines = (PageSectionAdmin,)


class PostAdmin(SummernoteModelAdmin): pass

admin.site.register(Post, PostAdmin)
# admin.site.register(Page, PageAdmin)
admin.site.register(Folder)
