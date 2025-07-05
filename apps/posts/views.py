from django.shortcuts import render  # , get_object_or_404
# from logging import warning

def view_posts(request, username=None, group_name=None):
    pass

def view_post(request, username=None, group_name=None, uuid=None):
    if not uuid:
        return view_posts(request, username, group_name)
    pass
