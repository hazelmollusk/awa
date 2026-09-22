from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import SiteLink


class SiteLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SiteLink
        fields = ("url", "name", "email", "role", "icon")
