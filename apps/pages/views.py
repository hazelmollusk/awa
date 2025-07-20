from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from logging import warning

from .models import Page


class ViewPageSet(APIView):
    def get(self, request, slug=None, uuuid=None, *args, **kwargs):
        page = get_object_or_404(Page, slug=slug)
        return render(
            request,
            "pages/page.html",
            {
                "page": page,
            },
        )
