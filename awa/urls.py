# from importlib import import_module
from django.contrib import admin
from django.urls import path, include
from django.contrib.sites.shortcuts import get_current_site
from django.conf.urls.static import static

# from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.conf import settings

from awa.settings import config
from apps.resume.views import ResumeViewSet

# from re import match

from .api import router
from .views import (
    stylesheet,
    script,
    login,
    logout,
)

from rest_framework import routers
from apps.pages.views import ViewPageSet
from .views import SiteLinkViewSet

app_name = "awa"

storage_urls = []
# list(
#     map(
#         storage_urls.extend,
#         [
#             static(v.base_url, document_root=v.location)
#             for _, v in config.storages.items()
#             if isinstance(v, dict) and v["type"] in ("local", "static", "default")
#         ],
#     )
# )

# storage_urls = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
#     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
# )

# user_urls = ([
#     path(f'{config.paths.blog}/',
#         include('apps.blog.urls', namespace='awa.blog')),
#     # path(f'{config.paths.profile}/', ...)
# ])


local_urls = (
    storage_urls
    + [
        path("css/<str:template_name>.css", stylesheet, name="stylesheet"),
        path("js/<str:template_name>.js", script, name="script"),
    ],
    app_name,
)

auth_urls = (
    [
        path("login/", login, name="login"),
        path("logout/", logout, name="logout"),
    ],
    "auth",
)

api_urls = (
    [
        path("api-auth", include("rest_framework.urls")),
    ],
    "api",
)

# user_model = get_user_model()
# anchor_urls = (
#     [
#         # path(f"{config.paths.user}/<path:path>", view_user),
#         # path(f"{config.paths.user}", view_user),
#     ],
#     app_name,
# )

urlpatterns = [
    path(f"{config.paths.i18n}/", include("django.conf.urls.i18n")),
    path(
        f"{config.paths.auth}/social/",
        include("social_django.urls", namespace="awa.social"),
    ),
    path(f"{config.paths.auth}/", include(auth_urls, namespace="awa.auth")),
    path(f"{config.paths.resources}/sn/", include("django_summernote.urls")),
    path(f"{config.paths.resources}/na/", include("nested_admin.urls")),
    path(
        f"{config.paths.api}/{config.paths.auth}/",
        include("rest_framework.urls", namespace="rest_framework"),
    ),
    path(f"{config.paths.api}/", include(router.urls)),
    path(f"{config.paths.admin}/", admin.site.urls),
    path(f"{config.paths.pages}/<slug:slug>/", ViewPageSet().as_view()),
    path("", include(local_urls)),
    path("~<str:username>/resume/", ResumeViewSet.as_view(), name="resume"),
    path("", ViewPageSet().as_view(), name="index"),
    # path("", include(anchor_urls)),
]
