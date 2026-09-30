from functools import cache

from .models import SiteLink

# from django.conf import settings
from django.contrib.sites.models import Site
from awa.settings import config

from apps.pages.models import Page
from django.contrib.contenttypes.models import ContentType


@cache
def awa(request):
    try:
        site = Site.objects.get_current(request)
    except Site.DoesNotExist:
        site = Site.objects.first()
    project = None
    for p in config.projects:
        for d in p.domains:
            if d.domain == site.domain:
                project = p
                break
        if project:
            break
    if not project:
        project = config.projects[0]

    context = {
        "links": {
            "menu": [],
            "header": SiteLink.objects.filter(role="header"),
            "footer": SiteLink.objects.filter(role="footer", icon__exact=""),
            "icons": SiteLink.objects.filter(role="footer").exclude(icon__exact=""),
        },
        "site": site,
        "config": config,
        "project": project,
    }
    return context
