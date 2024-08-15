from django.shortcuts import render  # , get_object_or_404
# from logging import warning
from apps.ara.decorators import context_view


@context_view("tuhi.Page")
def view_page(request, target, *args, **kwargs):
    return render(request, "pages/page.html", {"page": target, })
