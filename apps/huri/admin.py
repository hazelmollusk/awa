from django.contrib import admin

from .models import AwaTheme, AwaThemeIcon


class AwaIconAdmin(admin.TabularInline):
    fields = ['icon', 'icon_type']
    model = AwaThemeIcon
    # min_num = 1
    extra = 1


class AwaThemeAdmin(admin.ModelAdmin):
    model = AwaTheme
    inlines = [AwaIconAdmin]


# admin.site.register(Theme, ThemeAdmin)
admin.site.register(AwaTheme, AwaThemeAdmin)
