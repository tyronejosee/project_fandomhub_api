"""Serializers for Contents App."""

from rest_framework import serializers
from apps.categories.models import Studio, Genre, Season, Demographic


class StudioSerializer(serializers.ModelSerializer):
    """Serializer for Studio model."""
    image = serializers.CharField(source="get_image")

    class Meta:
        """Meta definition for StudioSerializer."""
        model = Studio
        fields = ["id", "slug", "name", "name_jpn", "established", "image",]
        read_only_fields = ["slug",]


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for Genre model."""

    class Meta:
        """Meta definition for GenreSerializer."""
        model = Genre
        fields = ["id", "name", "slug",]
        read_only_fields = ["slug",]


class SeasonSerializer(serializers.ModelSerializer):
    """Serializer for Season model."""

    class Meta:
        """Meta definition for SeasonSerializer."""
        model = Season
        fields = ["id", "season",]
        read_only_fields = ["id",]


class DemographicSerializer(serializers.ModelSerializer):
    """Serializer for Demographic model."""

    class Meta:
        """Meta definition for DemographicSerializer."""
        model = Demographic
        fields = ["id", "name",]
