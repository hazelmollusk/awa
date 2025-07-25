from django.contrib import admin

from guardian.admin import GuardedModelAdmin, GuardedModelAdminMixin
from mce_filebrowser.admin import MCEFilebrowserAdmin

from .models import Page, Folder, PageSection


AUDIT_FIELDS = ["created_by", "created", "modified"]


class PageSectionAdmin(admin.StackedInline):
    model = PageSection
    fields = ("title", "draft", "content")
    extra = 0
    min_num = 1


class PageAdmin(MCEFilebrowserAdmin):
    readonly_fields = AUDIT_FIELDS
    prepopulated_fields = {"slug": ["title"]}
    fieldsets = [
        (None, {"fields": ["title", "slug", "draft", "visible"]}),
        ("Audit", {"fields": AUDIT_FIELDS}),
    ]
    inlines = (PageSectionAdmin,)


admin.site.register(Page, PageAdmin)
admin.site.register(Folder)
