"""Serializers for Profiles App."""

from rest_framework import serializers

from apps.users.serializers import UserSerializer
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for Profile model."""
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "bio",
            "website",
            "birth_date",
            "image",
            "cover"
        ]
