"""Serializers for Utils App."""

from rest_framework import serializers

from .models import Picture


class PictureReadSerializer(serializers.ModelSerializer):
    """Serializer for Picture model (List/Retrieve)."""

    class Meta:
        model = Picture
        fields = [
            "id",
            "name",
            "image",
        ]


class PictureWriteSerializer(serializers.ModelSerializer):
    """Serializer for Picture model (Create/update)."""

    class Meta:
        model = Picture
        fields = [
            "name",
            "image",
        ]
        extra_kwargs = {
            "name": {"required": True},
            "image": {"required": True},
        }
