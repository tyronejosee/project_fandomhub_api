"""Serializers for Profiles App."""

from rest_framework import serializers

from apps.users.serializers import UserSerializer
from .models import Profile


class ProfileReadSerializer(serializers.ModelSerializer):
    """Serializer for Profile model (Retrieve)."""

    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "bio",
            "birth_date",
            "image",
            "cover",
        ]


class ProfileWriteSerializer(serializers.ModelSerializer):
    """Serializer for Profile model (Create/update)."""

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "bio",
            "birth_date",
            "image",
            "cover",
        ]
