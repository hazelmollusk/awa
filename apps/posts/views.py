from logging import warning
from django.shortcuts import get_object_or_404, render

from apps.people.models import Person  # , get_object_or_404
from .models import Post

# from logging import warning


def view_posts(request, username, *args, **kwargs):
    user = get_object_or_404(Person, username=username)
    posts = Post.objects.filter(created_by=user)
    return render(request, "posts/posts.html  ", {"posts": posts})


def view_post(request, username=None, uuid=None):
    warning(f"uuid: {uuid}")
    if not uuid:
        return view_posts(
            request,
        )
    if username:
        get_object_or_404(Person, username=username)
    post = get_object_or_404(Post, uuid=uuid)
    warning(f"post: {post}")
    return render(request, "posts/post.html", {"post": post})
