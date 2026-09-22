from django.urls import path, include

from awa.settings import config
from .views import view_post, view_posts
from .models import Post

urlpatterns = [
    path("<uuid:uuid>/", view_post, name="post_detail"),
    path("", view_posts, {"posts": Post.objects.all()}, name="post_list"),
    # path(f"{config.paths.posts}/", view_posts),
    # path(f"{config.paths.groups}/<slug:group_name>/{config.paths.posts}/<uuid:uuid>/", view_post),
    # path(f"{config.paths.groups}/<slug:group_name>/", view_posts),
    # path(f"~<str:username>/{config.paths.posts}/<uuid:uuid>/", view_post),
    # path(f"~<str:username>/", view_posts),
]
