"""Serializers for Producers App."""

from rest_framework import serializers

from apps.utils.validators import validate_name
from .models import Producer


class ProducerReadSerializer(serializers.ModelSerializer):
    """Serializer for Studio model (List/Retrieve)."""

    class Meta:
        model = Producer
        fields = [
            "id",
            "name",
            "name_jpn",
            "slug",
            "about",
            "established",
            "type",
            "image",
            "favorites",
            "created_at",
            "updated_at",
        ]


class ProducerWriteSerializer(serializers.ModelSerializer):
    """Serializer for Studio model (Create/update)."""

    name = serializers.CharField(validators=[validate_name])

    class Meta:
        model = Producer
        fields = [
            "name",
            "name_jpn",
            "about",
            "established",
            "type",
            "image",
        ]
        extra_kwargs = {
            "image": {"required": True},
        }
