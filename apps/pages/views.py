from django.shortcuts import render , get_object_or_404
# from logging import warning

from .models import Page

def view_page(request, slug, *args, **kwargs):
    page = get_object_or_404(Page, slug=slug)
    return render(request, "pages/page.html", {"page": page,})
