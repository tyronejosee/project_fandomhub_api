"""Serializers for Clubs App."""

from rest_framework import serializers

from .models import Club


class ClubReadSerializer(serializers.ModelSerializer):
    """Serializer for Club model (List/retrieve)."""

    class Meta:
        model = Club
        fields = [
            "id",
            "name",
            "description",
            "image",
            "category",
            "members",
            "created_by",
            "is_public",
            "created_at",
            "updated_at",
        ]


class ClubWriteSerializer(serializers.ModelSerializer):
    """Serializer for Club model (Create/update)."""

    class Meta:
        model = Club
        fields = [
            "name",
            "description",
            "image",
            "category",
            "is_public",
        ]
