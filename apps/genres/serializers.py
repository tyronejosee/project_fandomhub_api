"""Serializers for Genres App."""

from rest_framework import serializers

from apps.utils.validators import validate_name
from .models import Genre


class GenreReadSerializer(serializers.ModelSerializer):
    """Serializer for Genre model (List/retrieve)."""

    class Meta:
        model = Genre
        fields = [
            "id",
            "name",
            "slug",
            "created_at",
            "updated_at",
        ]


class GenreWriteSerializer(serializers.ModelSerializer):
    """Serializer for Genre model (Create/update)."""

    name = serializers.CharField(validators=[validate_name])

    class Meta:
        model = Genre
        fields = [
            "name",
        ]
