from functools import cache
from django.shortcuts import render, get_object_or_404  # , get_list_or_404
from .models import Post, PostType  # , PostComment, PostContent

POST_FETCH = 3


def post_qs(request):
    return Post.objects.get_for_user(request.user)


def post_list(request, offset=0, display=10, tag=None):
    posts = post_qs(request).published().posts()
    if tag:
        posts = posts.tagged(tag)
    posts = posts.order_by('-created')[offset: offset + display]
    return render(request, 'blog/post_list.html', {
        'posts': posts, 'tag': tag,
        'post_start': offset, 'post_display': display,
        'post_total': posts.count()
    })


def post_dispatch(request, slug=None, detail=False, published=True, username=None):
    posts = post_qs(request)
    # raise TypeError(slug)
    if published:
        posts = posts.published()
    if slug is None:
        post = posts.posts().order_by('-created').first()
        slug = post.slug
    else:
        post = get_object_or_404(posts, slug=slug)
    return post_highlight(request, post, detail) \
        if post.post_type == PostType.POST \
        else page(request, slug, post)


def post_highlight(request, post, detail=False):
    posts = post_qs(request).published().posts()
    # TODO: get previous/following in one query?
    previous = posts.filter(created__lt=post.created) \
        .order_by('-created')[0:POST_FETCH]
    following = posts.filter(created__gt=post.created) \
        .order_by('created')[0:POST_FETCH]
    return render(request, 'blog/post_highlight.html', {
        'post': post,
        'previous': previous,
        'following': following,
        'full': detail
    })


def page(request, slug, post=None):
    if not post:
        post = get_object_or_404(
            post_qs(request).published().all_pages(),
            slug=slug)
    return render(request, 'blog/page.html', {
        'page': post,
        'post': post,
    })
