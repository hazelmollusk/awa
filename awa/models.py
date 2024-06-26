from django.db import models
from apps.mana.models import AuditedMixin


class IconMixin(models.Model):
    icon = models.ImageField(
        upload_to="icons/",
        height_field="icon_height",
        width_field="icon_width",
        blank=True,
        null=True
    )
    icon_height = models.PositiveSmallIntegerField(blank=True, null=True)
    icon_width = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class ProjectLink(AuditedMixin, IconMixin):
    name = models.CharField(max_length=32)
    url = models.URLField(max_length=128)
    header = models.BooleanField(default=False)

    def __str__(self):
        return f"project link: {self.name}"
