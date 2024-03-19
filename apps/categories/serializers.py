"""Serializers for Contents App."""

from django.core.validators import RegexValidator
from rest_framework import serializers
from apps.categories.models import Studio, Genre, Theme, Season, Demographic
from apps.utils.validators import validate_name


class StudioListSerializer(serializers.ModelSerializer):
    """Serializer for Studio model (List only)."""

    class Meta:
        """Meta definition for StudioListSerializer."""
        model = Studio
        fields = ["id", "slug", "name"]
        read_only_fields = ["slug",]


class StudioSerializer(serializers.ModelSerializer):
    """Serializer for Studio model."""
    name = serializers.CharField(max_length=255, validators=[validate_name])

    class Meta:
        """Meta definition for StudioSerializer."""
        model = Studio
        fields = ["id", "slug", "name", "name_jpn", "established", "image",]
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


class SeasonListSerializer(serializers.ModelSerializer):
    """Serializer for Season model (List only)."""

    class Meta:
        """Meta definition for SeasonListSerializer."""
        model = Season
        fields = ["id", "fullname"]
        read_only_fields = ["id",]


class SeasonSerializer(serializers.ModelSerializer):
    """Serializer for Season model."""

    class Meta:
        """Meta definition for SeasonSerializer."""
        model = Season
        fields = ["id", "season", "year", "fullname"]
        read_only_fields = ["id", "fullname"]


class DemographicSerializer(serializers.ModelSerializer):
    """Serializer for Demographic model."""
    name = serializers.CharField(max_length=255, validators=[validate_name])

    class Meta:
        """Meta definition for DemographicSerializer."""
        model = Demographic
        fields = ["id", "name",]
