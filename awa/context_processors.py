from functools import cache

from .models import SiteLink

# from django.conf import settings
from django.contrib.sites.models import Site
from awa.settings import config

from apps.rakau.models import ContextRoot, ContentNode
from apps.tuhi.models import Page
from django.contrib.contenttypes.models import ContentType


@cache
def awa(request):
    try:
        site = Site.objects.get_current(request)
    except Site.DoesNotExist:
        site = Site.objects.first()
    project = config.get_current_project(request)
    root = ContextRoot.objects.get(sites=site)
    root_pages = ContentNode(
        parent=root, content_type=ContentType.objects.get_for_model(Page)
    )

    context = {
        "links": {
            "menu": root_pages,
            "header": SiteLink.objects.filter(role="header"),
            "footer": SiteLink.objects.filter(role="footer", icon__exact=""),
            "icons": SiteLink.objects.filter(role="footer").exclude(icon__exact=""),
        },
        "site": site,
        "config": config,
        "project": project,
    }
    return context
