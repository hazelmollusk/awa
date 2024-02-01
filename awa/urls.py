from importlib import import_module
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from .views import (
    blog, stylesheet, default,
    script, login, profile, logout,
)
from awa.settings import config
from django.conf.urls.static import static
from re import match

AWA_PATHS = [
    # global
    'admin',
    'auth',
    # per-user
    'blog',
    'profile',
]

config.setdefault('paths', {})
for url_path in AWA_PATHS:
    config.paths.setdefault(url_path, url_path)

#     serve(request, path, document_root=None, show_indexes=False)

storage_urls = []
list(map(storage_urls.extend, [
    static(v.url, document_root=v.root)
    for _, v in config.storage.items()
    if isinstance(v, dict) and v.type == 'local'
]))


# storage_urls = []
# for s, v in storage_classes:
#     if isinstance(v, str) and match(r'^[a-z][a-z\._]*[a-z]$', v):
#         module_parts = v.split('.')
#         func_name = module_parts.pop()
#         module_name = '.'.join(module_parts)
#         m = import_module(module_name)
#         f = getattr(m, func_name, None)
#         if callable(f):
#             p = path(config.storage[s].urlpattern, f, name=s)
#             storage_urls.append(p)

app_name = config.get('app_name', 'awa.app')

user_urls = ([
    path(f'{config.paths.blog}/',
        include('apps.blog.blog_v1.urls', namespace='awa.blog')),
    # path(f'{config.paths.profile}/', ...)
])

local_urls = (storage_urls + [
    path('css/<str:template_name>.css', stylesheet, name='stylesheet'),
    path('js/<str:template_name>.js', script, name='script'),
    path('', include(user_urls), kwargs={
        'username': config.default_username or None})
    # path('<str:slug>/', blog, name='blog'),
], app_name)

auth_urls = ([
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
], 'auth')


urlpatterns = [
    path(f'{config.paths.admin}/', admin.site.urls),
    path(f'{config.paths.blog}/',
        include('apps.blog.blog_v1.urls', namespace='awa.blog')),
    path(f'{config.paths.auth}/social/',
        include('social_django.urls', namespace='awa.social')),
    path(f'{config.paths.auth}/',
        include(auth_urls, namespace='awa.auth')),
    path(r'~<str:username>/', include(user_urls)),
    path('', include(local_urls, namespace='awa')),
]
