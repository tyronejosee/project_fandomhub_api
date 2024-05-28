"""Serializers for Profiles App."""

from rest_framework import serializers

from .models import Profile


class ProfileReadSerializer(serializers.ModelSerializer):
    """Serializer for Profile model (Retrieve)."""

    class Meta:
        model = Profile
        fields = [
            "id",
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
            "bio",
            "birth_date",
            "image",
            "cover",
        ]
