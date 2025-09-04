from django.shortcuts import get_object_or_404, render

from apps.people.models import Person  # , get_object_or_404
from .models import Post

# from logging import warning


def view_posts(request, username, *args, **kwargs):
    user = get_object_or_404(Person, username=username)
    posts = Post.objects.filter(created_by=user)
    return render(request, "posts/posts.html", {"posts": posts})


def view_post(request, uuid=None):
    if not uuid:
        return view_posts(
            request,
        )
    post = get_object_or_404(Post, uuid=uuid)
    return render(request, "posts/post.html", {"post": post})
