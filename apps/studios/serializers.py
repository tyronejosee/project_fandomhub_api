"""Serializers for Studios App."""

from rest_framework import serializers

from apps.utils.validators import validate_name
from .models import Studio


class StudioReadSerializer(serializers.ModelSerializer):
    """Serializer for Studio model (List/Retrieve)."""

    class Meta:
        model = Studio
        fields = [
            "id",
            "name",
            "name_jpn",
            "slug",
            "established",
            "image",
            "created_at",
            "updated_at",
        ]


class StudioWriteSerializer(serializers.ModelSerializer):
    """Serializer for Studio model (Create/update)."""

    name = serializers.CharField(validators=[validate_name])

    class Meta:
        model = Studio
        fields = [
            "name",
            "name_jpn",
            "established",
            "image",
        ]
        extra_kwargs = {
            "image": {"required": True},
        }
