"""Serializers for Contents App."""

from rest_framework import serializers

from apps.utils.validators import validate_name
from .models import Studio, Genre, Theme, Season, Demographic


class StudioSerializer(serializers.ModelSerializer):
    """Serializer for Studio model."""
    name = serializers.CharField(max_length=255, validators=[validate_name])

    class Meta:
        """Meta definition for StudioSerializer."""
        model = Studio
        fields = ["id", "slug", "name", "name_jpn", "established", "image",]
        read_only_fields = ["slug",]


class StudioListSerializer(serializers.ModelSerializer):
    """Serializer for Studio model (List only)."""

    class Meta:
        """Meta definition for StudioListSerializer."""
        model = Studio
        fields = ["id", "slug", "name"]
        read_only_fields = ["slug",]


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for Genre model."""
    name = serializers.CharField(max_length=255, validators=[validate_name])

    class Meta:
        """Meta definition for GenreSerializer."""
        model = Genre
        fields = ["id", "name", "slug",]
        read_only_fields = ["slug",]


class ThemeSerializer(serializers.ModelSerializer):
    """Serializer for Theme model."""
    name = serializers.CharField(max_length=255, validators=[validate_name])

    class Meta:
        """Meta definition for ThemeSerializer."""
        model = Theme
        fields = ["id", "name", "slug",]
        read_only_fields = ["slug",]


class SeasonSerializer(serializers.ModelSerializer):
    """Serializer for Season model."""

    class Meta:
        """Meta definition for SeasonSerializer."""
        model = Season
        fields = ["id", "season", "year", "fullname"]
        read_only_fields = ["id", "fullname"]


class SeasonListSerializer(serializers.ModelSerializer):
    """Serializer for Season model (List only)."""

    class Meta:
        """Meta definition for SeasonListSerializer."""
        model = Season
        fields = ["id", "fullname"]
        read_only_fields = ["id",]


class DemographicSerializer(serializers.ModelSerializer):
    """Serializer for Demographic model."""
    name = serializers.CharField(max_length=255, validators=[validate_name])

    class Meta:
        """Meta definition for DemographicSerializer."""
        model = Demographic
        fields = ["id", "name",]
