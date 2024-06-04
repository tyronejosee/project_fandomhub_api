"""Serializers for Utils App."""

from rest_framework import serializers

from .models import Picture, Video


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


class VideoReadSerializer(serializers.ModelSerializer):
    """Serializer for Video model (List/Retrieve)."""

    class Meta:
        model = Video
        fields = [
            "id",
            "video",
        ]


class VideoWriteSerializer(serializers.ModelSerializer):
    """Serializer for Video model (Create/Update)."""

    class Meta:
        model = Video
        fields = [
            "video",
        ]
