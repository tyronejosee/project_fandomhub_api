"""Serializers for Seasons App."""

from rest_framework import serializers

from .models import Season


class SeasonReadSerializer(serializers.ModelSerializer):
    """Serializer for Season model (List/Retrieve)."""

    class Meta:
        model = Season
        fields = [
            "id",
            "season",
            "year",
            "fullname",
            "created_at",
            "updated_at",
        ]


class SeasonWriteSerializer(serializers.ModelSerializer):
    """Serializer for Season model (Create/update)."""

    class Meta:
        model = Season
        fields = [
            "season",
            "year",
        ]
